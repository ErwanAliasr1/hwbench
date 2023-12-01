import pathlib

from .amd.amd import Amd
from .dell.dell import Dell
from .hpe.hpe import Hpe

from .vendor import Vendor
from .mock import MockVendor
from ..dmi import DmiSys


VENDOR_LIST = [
    Dell,
    Hpe,
    Amd,
]


def first_matching_vendor(out_dir: pathlib.Path, dmi: DmiSys) -> Vendor:
    for vendor in VENDOR_LIST:
        v = vendor(out_dir, dmi)  # type: ignore
        if v.detect():
            return v
    return MockVendor(out_dir, dmi)
