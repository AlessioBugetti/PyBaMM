#
# Tests for Ai (2020) Enertech parameter set loads
#
import pybamm
import unittest
import os


class TestAi2020(unittest.TestCase):
    def test_load_params(self):
        anode = pybamm.ParameterValues({}).read_parameters_csv(
            pybamm.get_parameters_filepath(
                "input/parameters/lithium-ion/anodes/graphite_Ai2020/parameters.csv"
            )
        )
        self.assertEqual(anode["Negative electrode porosity"], "0.33")

        cathode = pybamm.ParameterValues({}).read_parameters_csv(
            pybamm.get_parameters_filepath(
                "input/parameters/lithium-ion/cathodes/lico2_Ai2020/parameters.csv"
            )
        )
        self.assertEqual(cathode["Positive electrode porosity"], "0.32")

        electrolyte = pybamm.ParameterValues({}).read_parameters_csv(
            pybamm.get_parameters_filepath(
                "input/parameters/lithium-ion/electrolytes/lipf6_Enertech_Ai2020/"
                + "parameters.csv"
            )
        )
        self.assertEqual(electrolyte["Cation transference number"], "0.38")

        cell = pybamm.ParameterValues({}).read_parameters_csv(
            pybamm.get_parameters_filepath(
                "input/parameters/lithium-ion/cells/Enertech_Ai2020/parameters.csv"
            )
        )
        self.assertAlmostEqual(cell["Negative current collector thickness [m]"], 10e-6)

    def test_standard_lithium_parameters(self):

        chemistry = pybamm.parameter_sets.Ai2020
        parameter_values = pybamm.ParameterValues(chemistry=chemistry)

        model = pybamm.lithium_ion.DFN()
        sim = pybamm.Simulation(model, parameter_values=parameter_values)
        sim.set_parameters()
        sim.build()


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.settings.debug_mode = True
    unittest.main()
