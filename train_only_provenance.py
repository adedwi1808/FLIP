"""Small helpers for train-only FLIP provenance configuration."""


def source_dataset_versions(blind_target=None):
    """Return pinned provenance without requiring a target during train-only runs."""
    target = blind_target if isinstance(blind_target, dict) else {}
    surf = (
        "drive-master:historical-equivalence-UNVERIFIED"
        if target.get("provider") == "drive"
        else "adeedp/casia-surf/1"
    )
    return {
        "wmca": "adeedp/wmca-rgb/1",
        "casia_cefa": "adeedp/casia-cefa/2",
        "casia_surf": surf,
    }
