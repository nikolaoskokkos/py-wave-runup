from py_wave_runup import models
from pytest import raises, approx


class TestStockdon2006(object):
    def test_reflective(self):
        model = models.Stockdon2006(Hs=4, Tp=11, beta=0.1)
        assert model.R2 == approx(2.54, abs=0.01)
        assert model.setup == approx(0.96, abs=0.01)
        assert model.sig == approx(1.65, abs=0.01)
        assert model.sinc == approx(2.06, abs=0.01)
        assert model.swash == approx(2.64, abs=0.01)

    def test_dissipative(self):
        model = models.Stockdon2006(Hs=4, Tp=11, beta=0.001)
        assert model.R2 == approx(1.18, abs=0.01)
        assert model.setup == approx(0.0096, abs=0.01)
        assert model.sig == approx(1.65, abs=0.01)
        assert model.sinc == approx(0.02, abs=0.01)
        assert model.swash == approx(1.65, abs=0.01)

    def test_wave_length(self):
        model = models.Stockdon2006(Hs=4, Lp=200, beta=0.05)
        assert model.R2 == approx(1.69, 0.1)

    def test_list_input(self):
        model = models.Stockdon2006(Hs=[1, 2], Lp=[100, 200], beta=[0.05, 0.1])
        assert model.R2 == approx((0.59, 1.84), abs=0.1)
        assert model.setup == approx((0.17, 0.70), abs=0.1)
        assert model.sig == approx((0.6, 1.2), abs=0.1)
        assert model.sinc == approx((0.37, 1.5), abs=0.1)
        assert model.swash == approx((0.71, 1.92), abs=0.01)

    def test_no_wave_length(self):
        with raises(ValueError):
            models.Stockdon2006(Hs=1, beta=0.1)

    def test_different_list_input(self):
        with raises(ValueError):
            models.Stockdon2006(Hs=[1, 2], Lp=[100, 200], beta=[0.1])


class TestPower2018(object):
    def test_reflective(self):
        model = models.Power2018(Hs=4, Tp=11, beta=0.1, r=0.00075)
        assert model.R2 == approx(4.79, abs=0.01)

    def test_dissipative(self):
        model = models.Power2018(Hs=4, Tp=11, beta=0.001, r=0.00075)
        assert model.R2 == approx(33.75, abs=0.01)

    def test_low_wave_conditions(self):
        model = models.Power2018(Hs=1, Tp=8, beta=0.07, r=0.00075)
        assert model.R2 == approx(1.12, abs=0.01)

    def test_list_input(self):
        model = models.Power2018(
            Hs=[1, 2], Lp=[100, 200], beta=[0.05, 0.1], r=[0.00075, 0.00075]
        )
        assert model.R2 == approx((0.922, 2.88), abs=0.1)

    def test_no_roughness(self):
        with raises(ValueError):
            model = models.Power2018(Hs=4, Tp=11, beta=0.1)
