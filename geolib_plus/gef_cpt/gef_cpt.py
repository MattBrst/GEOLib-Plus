from geolib_plus.cpt_base_model import AbstractCPT, CptReader
from .gef_file_reader import GefFileReader
from pathlib import Path


class GefCpt(AbstractCPT):
    @classmethod
    def get_cpt_reader(self) -> CptReader:
        return GefFileReader
