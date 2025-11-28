# Auto-generated from MRtrix C++ command with '__print_pydra_code__' secret option

from typing import Any
from pathlib import Path  # noqa: F401
from fileformats.generic import File, Directory  # noqa: F401
from fileformats.vendor.mrtrix3.medimage import ImageIn, ImageOut, Tracks  # noqa: F401
from pydra.compose import shell
from pydra.utils.typing import MultiInputObj


@shell.define
class MrCalc(shell.Task["MrCalc.Outputs"]):
    """This command will only compute per-voxel operations. Use 'mrmath' to compute summary statistics across images or along image axes.

        This command uses a stack-based syntax, with operators (specified using options) operating on the top-most entries (i.e. images or values) in the stack. Operands (values or images) are pushed onto the stack in the order they appear (as arguments) on the command-line, and operators (specified as options) operate on and consume the top-most entries in the stack, and push their output as a new entry on the stack.

        As an additional feature, this command will allow images with different dimensions to be processed, provided they satisfy the following conditions: for each axis, the dimensions match if they are the same size, or one of them has size one. In the latter case, the entire image will be replicated along that axis. This allows for example a 4D image of size [ X Y Z N ] to be added to a 3D image of size [ X Y Z ], as if it consisted of N copies of the 3D image along the 4th axis (the missing dimension is assumed to have size 1). Another example would a single-voxel 4D image of size [ 1 1 1 N ], multiplied by a 3D image of size [ X Y Z ], which would allow the creation of a 4D image where each volume consists of the 3D image scaled by the corresponding value for that volume in the single-voxel image.

        The following special keywords are permitted as operands on the stack: 'rand' (random number between 0 and 1); 'randn' (random number from unit std.dev. normal distribution); 'e' (Euler's number); 'pi' (ratio of circumference of circle to diameter)


        Example usages
        --------------


        Double the value stored in every voxel:

        `$ mrcalc a.mif 2 -mult r.mif`

        This performs the operation:  r = 2*a  for every voxel a,r in images a.mif and r.mif respectively.


        A more complex example:

        `$ mrcalc a.mif -neg b.mif -div -exp 9.3 -mult r.mif`

        This performs the operation: r = 9.3*exp(-a/b)


        Another complex example:

        `$ mrcalc a.mif b.mif -add c.mif d.mif -mult 4.2 -add -div r.mif`

        This performs: r = (a+b)/(c*d+4.2).


        Rescale the densities in a SH l=0 image:

        `$ mrcalc ODF_CSF.mif 4 pi -mult -sqrt -div ODF_CSF_scaled.mif`

        This applies the spherical harmonic basis scaling factor: 1.0/sqrt(4*pi), such that a single-tissue voxel containing the same intensities as the response function of that tissue should contain the value 1.0.


        References
        ----------

            Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137


        MRtrix
        ------

        Version:3.0.7-1578-g23fff5b8-dirty, built Nov 28 2025

        Author: J-Donald Tournier (jdtournier@gmail.com)

        Copyright: Copyright (c) 2008-2025 the MRtrix3 contributors.

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.

    Covered Software is provided under this License on an "as is"
    basis, without warranty of any kind, either expressed, implied, or
    statutory, including, without limitation, warranties that the
    Covered Software is free of defects, merchantable, fit for a
    particular purpose or non-infringing.
    See the Mozilla Public License v. 2.0 for more details.

    For more details, see http://www.mrtrix.org/.
    """

    executable = "mrcalc"

    # Arguments

    # Options

    # basic operations:
    abs: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-abs",
        help="""|%1| : return absolute value (magnitude) of real or complex number""",
    )
    neg: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-neg",
        help="""-%1 : negative value""",
    )
    add: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-add",
        help="""(%1 + %2) : add values""",
    )
    subtract: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-subtract",
        help="""(%1 - %2) : subtract nth operand from (n-1)th""",
    )
    multiply: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-multiply",
        help="""(%1 * %2) : multiply values""",
    )
    divide: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-divide",
        help="""(%1 / %2) : divide (n-1)th operand by nth""",
    )
    modulo: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-modulo",
        help="""(%1 % %2) : remainder after dividing (n-1)th operand by nth""",
    )
    min: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-min",
        help="""min (%1, %2) : smallest of last two operands""",
    )
    max: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-max",
        help="""max (%1, %2) : greatest of last two operands""",
    )

    # comparison operators:
    lt: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-lt",
        help="""(%1 < %2) : less-than operator (true=1, false=0)""",
    )
    gt: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-gt",
        help="""(%1 > %2) : greater-than operator (true=1, false=0)""",
    )
    le: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-le",
        help="""(%1 <= %2) : less-than-or-equal-to operator (true=1, false=0)""",
    )
    ge: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-ge",
        help="""(%1 >= %2) : greater-than-or-equal-to operator (true=1, false=0)""",
    )
    eq: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-eq",
        help="""(%1 == %2) : equal-to operator (true=1, false=0)""",
    )
    neq: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-neq",
        help="""(%1 != %2) : not-equal-to operator (true=1, false=0)""",
    )

    # conditional operators:
    if_: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-if",
        help="""(%1 ? %2 : %3) : if first operand is true (non-zero), return second operand, otherwise return third operand""",
    )
    replace: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-replace",
        help="""(%1, %2 -> %3) : Wherever first operand is equal to the second operand, replace with third operand""",
    )

    # power functions:
    sqrt: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-sqrt",
        help="""sqrt (%1) : square root""",
    )
    pow: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-pow",
        help="""%1^%2 : raise (n-1)th operand to nth power""",
    )

    # nearest integer operations:
    round: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-round",
        help="""round (%1) : round to nearest integer""",
    )
    ceil: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-ceil",
        help="""ceil (%1) : round up to nearest integer""",
    )
    floor: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-floor",
        help="""floor (%1) : round down to nearest integer""",
    )

    # logical operators:
    not_: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-not",
        help="""!%1 : NOT operator: true (1) if operand is false (i.e. zero)""",
    )
    and_: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-and",
        help="""(%1 && %2) : AND operator: true (1) if both operands are true (i.e. non-zero)""",
    )
    or_: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-or",
        help="""(%1 || %2) : OR operator: true (1) if either operand is true (i.e. non-zero)""",
    )
    xor: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-xor",
        help="""(%1 ^^ %2) : XOR operator: true (1) if only one of the operands is true (i.e. non-zero)""",
    )

    # classification functions:
    isnan: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-isnan",
        help="""isnan (%1) : true (1) if operand is not-a-number (NaN)""",
    )
    isinf: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-isinf",
        help="""isinf (%1) : true (1) if operand is infinite (Inf)""",
    )
    finite: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-finite",
        help="""finite (%1) : true (1) if operand is finite (i.e. not NaN or Inf)""",
    )

    # complex numbers:
    complex: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-complex",
        help="""(%1 + %2 i) : create complex number using the last two operands as real,imaginary components""",
    )
    polar: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-polar",
        help="""(%1 /_ %2) : create complex number using the last two operands as magnitude,phase components (phase in radians)""",
    )
    real: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-real",
        help="""real (%1) : real part of complex number""",
    )
    imag: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-imag",
        help="""imag (%1) : imaginary part of complex number""",
    )
    phase: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-phase",
        help="""phase (%1) : phase of complex number (use -abs for magnitude)""",
    )
    conj: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-conj",
        help="""conj (%1) : complex conjugate""",
    )
    proj: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-proj",
        help="""proj (%1) : projection onto the Riemann sphere""",
    )

    # exponential functions:
    exp: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-exp",
        help="""exp (%1) : exponential function""",
    )
    log: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-log",
        help="""log (%1) : natural logarithm""",
    )
    log10: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-log10",
        help="""log10 (%1) : common logarithm""",
    )

    # trigonometric functions:
    cos: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-cos",
        help="""cos (%1) : cosine""",
    )
    sin: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-sin",
        help="""sin (%1) : sine""",
    )
    tan: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-tan",
        help="""tan (%1) : tangent""",
    )
    acos: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-acos",
        help="""acos (%1) : inverse cosine""",
    )
    asin: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-asin",
        help="""asin (%1) : inverse sine""",
    )
    atan: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-atan",
        help="""atan (%1) : inverse tangent""",
    )

    # hyperbolic functions:
    cosh: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-cosh",
        help="""cosh (%1) : hyperbolic cosine""",
    )
    sinh: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-sinh",
        help="""sinh (%1) : hyperbolic sine""",
    )
    tanh: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-tanh",
        help="""tanh (%1) : hyperbolic tangent""",
    )
    acosh: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-acosh",
        help="""acosh (%1) : inverse hyperbolic cosine""",
    )
    asinh: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-asinh",
        help="""asinh (%1) : inverse hyperbolic sine""",
    )
    atanh: MultiInputObj[bool] | None = shell.arg(
        default=None,
        argstr="-atanh",
        help="""atanh (%1) : inverse hyperbolic tangent""",
    )

    # Data type options:
    datatype: str | None = shell.arg(
        default=None,
        argstr="-datatype",
        help="""specify output image data type. Valid choices are: float16, float16le, float16be, float32, float32le, float32be, float64, float64le, float64be, int64, uint64, int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le, int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be, cfloat16, cfloat16le, cfloat16be, cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be, int8, uint8, bit.""",
        allowed_values=[
            "float16",
            "float16le",
            "float16be",
            "float32",
            "float32le",
            "float32be",
            "float64",
            "float64le",
            "float64be",
            "int64",
            "uint64",
            "int64le",
            "uint64le",
            "int64be",
            "uint64be",
            "int32",
            "uint32",
            "int32le",
            "uint32le",
            "int32be",
            "uint32be",
            "int16",
            "uint16",
            "int16le",
            "uint16le",
            "int16be",
            "uint16be",
            "cfloat16",
            "cfloat16le",
            "cfloat16be",
            "cfloat32",
            "cfloat32le",
            "cfloat32be",
            "cfloat64",
            "cfloat64le",
            "cfloat64be",
            "int8",
            "uint8",
            "bit",
        ],
    )

    # Standard options
    info: bool = shell.arg(
        default=False,
        argstr="-info",
        help="""display information messages.""",
    )
    quiet: bool = shell.arg(
        default=False,
        argstr="-quiet",
        help="""do not display information messages or progress status; alternatively, this can be achieved by setting the MRTRIX_QUIET environment variable to a non-empty string.""",
    )
    debug: bool = shell.arg(
        default=False,
        argstr="-debug",
        help="""display debugging messages.""",
    )
    force: bool = shell.arg(
        default=False,
        argstr="-force",
        help="""force overwrite of output files (caution: using the same file as input and output might cause unexpected behaviour).""",
    )
    nthreads: int | None = shell.arg(
        default=None,
        argstr="-nthreads",
        help="""use this number of threads in multi-threaded applications (set to 0 to disable multi-threading).""",
    )
    config: MultiInputObj[tuple[str, str]] | None = shell.arg(
        default=None,
        argstr="-config",
        help="""temporarily set the value of an MRtrix config file entry.""",
        sep=" ",
    )

    class Outputs(shell.Outputs):
        operand: list[str | float | ImageIn | ImageOut] = shell.outarg(
            argstr="",
            position=1,
            path_template="operand.mif",
            help="""an input image, intensity value, or special keyword (see Description)""",
        )
