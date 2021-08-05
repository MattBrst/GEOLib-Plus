import pytest
import math
import numpy as np
from tests.utils import TestUtils
from geolib_plus.soft_soil_creep_parameters import SoftSoilCreepParameters


class TestSoftSoilCreepParameters:
    def test_calculate_soft_soil_parameters(self):

        # define inputs for the model as floats
        eo = 0.8
        v_ur = 0.5
        Cc = 1.15 * (eo - 0.35)
        Cs = 0.5
        Ca = 0.1
        # define some as arrays
        OCR = np.array([1, 2, 2, 10])
        K0_NC = np.array([1, 2, 2, 10])
        # initialize class and check initial expectations
        parameters_for_SSC = SoftSoilCreepParameters(
            eo=eo, OCR=OCR, v_ur=v_ur, Cc=Cc, Cs=Cs, K0_NC=K0_NC, Ca=Ca
        )
        assert parameters_for_SSC
        # run test
        parameters_for_SSC.calculate_soft_soil_parameters()
        # check results
        assert parameters_for_SSC.kappa is not None
        assert parameters_for_SSC.lamda is not None
        assert parameters_for_SSC.mu is not None
