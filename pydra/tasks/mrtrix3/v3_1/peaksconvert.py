# Auto-generated from MRtrix C++ command with '__print_pydra_code__' secret option

from typing import Any
from pathlib import Path  # noqa: F401
from fileformats.generic import File, Directory  # noqa: F401
from fileformats.vendor.mrtrix3.medimage import ImageIn, ImageOut, Tracks  # noqa: F401
from pydra.compose import shell
from pydra.utils.typing import MultiInputObj


@shell.define
class PeaksConvert(shell.Task["PeaksConvert.Outputs"]):
    """Under default operation with no command-line options specified, the output image will be identical to the input image, as the MRtrix convention (3-vectors defined with respect to RAS scanner space axes) will be assumed to apply to both cases. This behaviour is only modulated by explicitly providing command-line options that give additional information about the format or reference of either input or output images.

        For -in_format and -out_format options, the choices are: - "unitspherical": Each orientation is represented using 2 sequential volumes encoded as azimuth and inclination angles in radians; - "spherical": Each orientation and associated value is represented using 3 sequential volumes, with associated value ("radius") first, followed by aximuth and inclination angles in radians; - "unit3vector": Each orientation is represented using 3 sequential volumes encoded as three dot products with respect to three orthogonal reference axes; - "3vector": Each orientation and associated non-negative value is represented using 3 sequential volumes, with the norm of that 3-vector encoding the associated value and the unit-normalised vector encoding the three dot products with respect to three orthogonal reference axes. The default behaviour throughout MRtrix3 is to interpret data as either "unit3vector" or "3vector" depending upon the context and/or presence of non-unit norm vectors in the data.

        For -in_reference and -out_reference options, the choices are: - "xyz": Directions are defined with respect to "real space" / "scanner space", which is independent of the transform stored within the image header, with the assumption that the positive direction of the first axis is that closest to anatomical right, the positive direction of the second axis is that closest to anatomical anterior, and the positive direction of the third axis is that closest to anatomical superior (so-called "RAS+"); - "ijk": Directions are defined with respect to the image axes as represented on the file system; - "fsl": Directions are defined with respect to the internal convention adopted by the FSL software, which is equivalent to "ijk" for images with a negative header transform determinant (so-called "left-handed" coordinate systems) but for images with a positive header transform determinant (which is the case for the "RAS+" convention adopted for both NIfTI and MRtrix3) the interpretation is equivalent to being with respect to the image axes after flipping the first image axis. The default interpretation in MRtrix3, including for this command in the absence of use of one of the command-line options, is "xyz".


        References
        ----------

            Tournier, J.-D.; Smith, R. E.; Raffelt, D.; Tabbara, R.; Dhollander, T.; Pietsch, M.; Christiaens, D.; Jeurissen, B.; Yeh, C.-H. & Connelly, A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. NeuroImage, 2019, 202, 116137


        MRtrix
        ------

        Version:3.0.7-1583-g24a09ac5-dirty, built Dec  3 2025

        Author: Robert E. Smith (robert.smith@florey.edu.au)

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

    executable = "peaksconvert"

    # Arguments
    in_file: ImageIn = shell.arg(
        argstr="",
        position=1,
        help="""the input directions image""",
    )

    # Options

    # Options providing information about the input image:
    in_format: str | None = shell.arg(
        default=None,
        argstr="-in_format",
        help="""specify the format in which the input directions are specified (see Description)""",
        allowed_values=["unitspherical", "spherical", "unit3vector", "3vector"],
    )
    in_reference: str | None = shell.arg(
        default=None,
        argstr="-in_reference",
        help="""specify the reference axes against which the input directions are specified (see Description)""",
        allowed_values=["xyz", "ijk", "fsl"],
    )

    # Options providing information about the output image:
    out_format: str | None = shell.arg(
        default=None,
        argstr="-out_format",
        help="""specify the format in which the output directions will be specified (see Description)""",
        allowed_values=["unitspherical", "spherical", "unit3vector", "3vector"],
    )
    out_reference: str | None = shell.arg(
        default=None,
        argstr="-out_reference",
        help="""specify the reference axes against which the output directions will be specified (see Description)""",
        allowed_values=["xyz", "ijk", "fsl"],
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
        out_file: ImageOut = shell.outarg(
            argstr="",
            position=2,
            path_template="out_file.mif",
            help="""the output directions image""",
        )
