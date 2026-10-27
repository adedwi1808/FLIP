import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from train_only_provenance import source_dataset_versions


def test_train_only_target_may_be_null():
    versions = source_dataset_versions(None)
    assert versions == {
        "wmca": "adeedp/wmca-rgb/1",
        "casia_cefa": "adeedp/casia-cefa/2",
        "casia_surf": "adeedp/casia-surf/1",
    }


def test_null_target_is_same_as_omitted_target():
    assert source_dataset_versions(None) == source_dataset_versions()


def test_drive_target_provenance_is_explicitly_unverified():
    versions = source_dataset_versions({"provider": "drive"})
    assert versions["casia_surf"] == "drive-master:historical-equivalence-UNVERIFIED"
