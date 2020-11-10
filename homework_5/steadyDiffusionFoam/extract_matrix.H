void addToInternalField
(
    const labelUList& addr,
    const scalarField& pf,
    scalarField& intf
) 
{
    if (addr.size() != pf.size())
    {
        FatalErrorIn
        (
            "addToInternalField(const labelUList&, "
            "const Field&, Field&)"
        )   << "sizes of addressing and field are different"
            << abort(FatalError);
    }

    forAll(addr, faceI)
    {
        intf[addr[faceI]] += pf[faceI];
    }
}

scalarSquareMatrix convert
(
    const lduMatrix& ldum
)
{
    const label* __restrict__ uPtr = ldum.lduAddr().upperAddr().begin();
    const label* __restrict__ lPtr = ldum.lduAddr().lowerAddr().begin();

    const scalar* __restrict__ diagPtr = ldum.diag().begin();
    const scalar* __restrict__ upperPtr = ldum.upper().begin();
    const scalar* __restrict__ lowerPtr = ldum.lower().begin();

    register const label nCells = ldum.diag().size();
    register const label nFaces = ldum.upper().size();

    //construct a square matrix and initialize to zero
    scalarSquareMatrix ssMatrix(nCells);
    for(int i=0;i<ssMatrix.n();i++)
       for(int j=0;j<ssMatrix.n();j++)
           ssMatrix.operator[](i)[j] = 0.0;
     
    for (register label cell=0; cell<nCells; cell++)
    {
        ssMatrix.operator[](cell)[cell] = diagPtr[cell];
    }

    for (register label face=0; face<nFaces; face++)
    {
        label uCell = uPtr[face];
        label lCell = lPtr[face];

        ssMatrix.operator[](uCell)[lCell] = lowerPtr[face];
        ssMatrix.operator[](lCell)[uCell] = upperPtr[face];
    }

    return ssMatrix;
}

//save the matrix and source term to files
//After discretization, the governing equation becomes a 
//linear system Ax=b. 
//Note: fvScalarMatrix usually does not consider the effect of 
//      boundary conditions. B.C. are assemled to the matrix and 
//      source right before the solve step.
int saveMatrix(fvScalarMatrix ofMatrix) 
{
	const lduMatrix& ofLDUMatrix = static_cast<const lduMatrix&>(ofMatrix);

        scalarSquareMatrix ssMatrix = convert(ofLDUMatrix);

        //consider the boundary effect on the matrix and the source term
        scalarField saveDiag(ofMatrix.diag());

        //hack of fvMatrix::addBoundaryDiag member function 
        //it is protected, so I don't access from outside
        forAll(ofMatrix.internalCoeffs(), patchI)
        {
             addToInternalField
             (
                 ofMatrix.lduAddr().patchAddr(patchI),
                 ofMatrix.internalCoeffs()[patchI].component(0),
                 saveDiag
              );
        }

        //set the diagonal of the ssMatrix as the B.C. corrected one
        for(int i=0;i<ssMatrix.n();i++)
        {
               ssMatrix.operator[](i)[i] = saveDiag[i];
        }

        scalarField totalSource(ofMatrix.source());

        //hack of fvMatrix::addBoundarySource member function 
        forAll(ofMatrix.psi().boundaryField(), patchI)
        {
            const fvPatchField<scalar>& ptf = 
                        ofMatrix.psi().boundaryField()[patchI];
            const scalarField& pbc = ofMatrix.boundaryCoeffs()[patchI];

            if (!ptf.coupled())
            {
                addToInternalField
                (
                   ofMatrix.lduAddr().patchAddr(patchI),
                   pbc,
                   totalSource
                 );
             }
             else
             {
                 FatalErrorIn
                 (
                    "This addBoundarySource routine "
                  )   << "should not be used with coupled boundaries"
                  << abort(FatalError);
             }
        }

        //set the diagonal and source of the ssMatrix as the B.C. corrected one
        for(int i=0;i<ssMatrix.n();i++)
        {
             ssMatrix.operator[](i)[i] = saveDiag[i];
             ofMatrix.source()[i] = totalSource[i];
        }

        register const label nCells = ofLDUMatrix.diag().size();
	Info << "Writing " << nCells 
             << "x"<< nCells << " cells "  << endl; 

        // write to file
	FILE * matrixFile = fopen("matrix.dat" ,"w");
	FILE * srcFile = fopen("src.dat" ,"w");
        
	if (matrixFile == NULL) 
        {
	    Info << "Could not open file matrix.dat!" << endl;
	    return -1;
	}
        if (srcFile == NULL) 
        {
            Info << "Could not open file src.dat!" << endl;
            return -1;
        }


	for (int x=0;x<nCells; x++) 
        {
	  for (int y=0;y<nCells; y++) 
          {
	      fprintf(matrixFile, "%5.2f ", (ssMatrix.operator[](y)[x]));
	  }
          fprintf(srcFile, "%5.2f ", ofMatrix.source()[x]);

	  fprintf(matrixFile, "\n");
          fprintf(srcFile, "\n");
	}
	
	if (fclose(matrixFile) != 0) 
        {
	  Info << "Could not close matrix file!"<< endl;
	  return -1;
	}

        if (fclose(srcFile) != 0) 
        {
          Info << "Could not close src file!"<< endl;
          return -1;
        }
	
	Info << "All cells successfully written to file!" << endl;

    return 0;	
}
