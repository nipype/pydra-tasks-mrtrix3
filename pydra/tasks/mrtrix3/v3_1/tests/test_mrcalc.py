# Auto-generated test for mrcalc

import pytest
from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.vendor.mrtrix3.medimage import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_1 import MrCalc


@pytest.mark.xfail
def test_mrcalc(tmp_path, cli_parse_only):

    task = MrCalc(
        abs=None,
        acos=None,
        acosh=None,
        add=None,
        and_=None,
        asin=None,
        asinh=None,
        atan=None,
        atanh=None,
        ceil=None,
        complex=None,
        conj=None,
        cos=None,
        cosh=None,
        datatype=None,
        debug=False,
        divide=None,
        eq=None,
        exp=None,
        finite=None,
        floor=None,
        force=False,
        ge=None,
        gt=None,
        if_=None,
        imag=None,
        isinf=None,
        isnan=None,
        le=None,
        log=None,
        log10=None,
        lt=None,
        max=None,
        min=None,
        modulo=None,
        multiply=None,
        neg=None,
        neq=None,
        not_=None,
        or_=None,
        phase=None,
        polar=None,
        pow=None,
        proj=None,
        real=None,
        replace=None,
        round=None,
        sin=None,
        sinh=None,
        sqrt=None,
        subtract=None,
        tan=None,
        tanh=None,
        xor=None,
        operand=list(["a-string"]),
    )
    result = task(worker="debug")
    assert not result.errored
