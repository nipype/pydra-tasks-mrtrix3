# Auto-generated test for peakscheck

import pytest
from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.vendor.mrtrix3.medimage import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_1 import PeaksCheck


@pytest.mark.xfail
def test_peakscheck(tmp_path, cli_parse_only):

    task = PeaksCheck(
        all=False,
        cont=None,
        debug=False,
        force=False,
        format=None,
        in_file=Nifti1.sample(),
        mask=None,
        nocleanup=False,
        noshuffle=False,
        notransform=False,
        number=None,
        reference=None,
        scratch=None,
        threshold=None,
        out_table=None,
    )
    result = task(worker="debug")
    assert not result.errored
