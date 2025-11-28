# Auto-generated test for dwirecon

import pytest
from fileformats.generic import File, Directory, FsObject  # noqa
from fileformats.medimage import Nifti1  # noqa
from fileformats.vendor.mrtrix3.medimage import ImageFormat, ImageIn, Tracks  # noqa
from pydra.tasks.mrtrix3.v3_1 import DwiRecon


@pytest.mark.xfail
def test_dwirecon(tmp_path, cli_parse_only):

    task = DwiRecon(
        debug=False,
        exponent=None,
        field=None,
        force=False,
        fslgrad=None,
        grad=None,
        import_pe_eddy=None,
        import_pe_table=None,
        import_pe_topup=None,
        in_file=Nifti1.sample(),
        lmax=None,
        operation="combine_pairs",
        pairs_in=None,
        export_grad_fsl=None,
        export_grad_mrtrix=None,
        out_file=File.sample(),
        pairs_out=None,
        predicted=None,
        weights=None,
    )
    result = task(worker="debug")
    assert not result.errored
