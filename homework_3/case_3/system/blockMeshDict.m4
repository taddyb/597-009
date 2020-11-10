/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  8.0                                   |
|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    object      blockMeshDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
//
dnl> -----------------------------------------------------------------
dnl> <STANDARD DEFINTIONS>
dnl>
changecom(//)changequote([,]) dnl>
define(calc, [esyscmd(perl -e 'print ($1)')]) dnl>
define(VCOUNT, 0)  dnl>
define(vlabel, [[// ]pt VCOUNT ($1) define($1, VCOUNT)define([VCOUNT], incr(VCOUNT))])  dnl>
dnl>
define(hex2D, hex ($1f $2f $3f $4f $1b $2b $3b $4b)) dnl>
dnl>
dnl> </STANDARD DEFINTIONS>
dnl> -----------------------------------------------------------------
dnl>

//refine times
define(refine, 100) dnl>

define(n1,calc(refine*.6)) dnl>
define(n2,calc(refine* 1)) dnl>
define(n3,calc(refine*.4)) dnl>
define(n4,1) dnl>

define(L1,4)          //domain length 2, lower cavity  width/height
define(L2,10)            //domain length 3, upper cavity  width/height
define(L3,0.1)        //z-axis (small number)

define(x0,0) dnl>
define(x1,calc(L2-L1)) dnl>
define(x2,calc(L2-L1)) dnl>
define(x3,calc(L2)) dnl>
define(x4,calc(L2)) dnl>
define(x5,calc(L2)) dnl>
define(x6,calc(L2-L1)) dnl>
define(x7,0) dnl>

define(y0,0) dnl>
define(y1,0) dnl>
define(y2,calc(-L1)) dnl>
define(y3,calc(-L1)) dnl>
define(y4,0) dnl>
define(y5,calc(L2)) dnl>
define(y6,calc(L2)) dnl>
define(y7,calc(L2)) dnl>

define(zFront,0) dnl>
define(zBack, calc(L3)) dnl>

convertToMeters 1;

vertices
(
    //vertex on the front
    (x0   y0 zFront)  vlabel(a0f)
    (x1   y1 zFront)  vlabel(a1f)
    (x2   y2 zFront)  vlabel(a2f)
    (x3   y3 zFront)  vlabel(a3f)
    (x4   y4 zFront)  vlabel(a4f)
    (x5   y5 zFront)  vlabel(a5f)
    (x6   y6 zFront)  vlabel(a6f)
    (x7   y7 zFront)  vlabel(a7f)

    //vertex on back
    (x0   y0 zBack)  vlabel(a0b)
    (x1   y1 zBack)  vlabel(a1b)
    (x2   y2 zBack)  vlabel(a2b)
    (x3   y3 zBack)  vlabel(a3b)
    (x4   y4 zBack)  vlabel(a4b)
    (x5   y5 zBack)  vlabel(a5b)
    (x6   y6 zBack)  vlabel(a6b)
    (x7   y7 zBack)  vlabel(a7b)
);

blocks
(
    // block 1
    hex2D(a0, a1, a6, a7)
    block1 (n1 n2 n4) simpleGrading (1 1 1)

    // block 2
    hex2D(a1, a4, a5, a6)
    block2 (n3 n2 n4) simpleGrading (1 1 1)

    //block 3
    hex2D(a2, a3, a4, a1)
    block3 (n3 n3 n4) simpleGrading (1 1 1)
);

edges
(
);

boundary
(
    movingWall
    {
        type wall;
        faces
        (
            (7 15 14 6)
            (6 14 13 5)
        );
    }
    fixedWalls
    {
        type wall;
        faces
        (
            (0 8 15 7)
            (4 12 13 5)
            (3 11 12 4)
            (0 8 9 1)
            (2 10 9 1)
            (2 10 11 3)
        );
    }
    frontAndBack
    {
        type empty;
        faces
        (
            (0 1 6 7)
            (1 4 5 6)
            (2 3 4 1)
            (8 9 14 15)
            (9 12 13 14)
            (10 11 12 9)
        );
    }
);


mergePatchPairs
(
);

// ************************************************************************* //
