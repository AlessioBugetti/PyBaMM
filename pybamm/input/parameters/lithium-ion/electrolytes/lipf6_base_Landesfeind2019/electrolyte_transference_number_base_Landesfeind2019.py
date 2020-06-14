def electrolyte_transference_number_base_Landesfeind2019(c_e, T, coeffs):
    """
    Transference number of LiPF6 in solvent_X as a function of ion concentration and
    temperature. The data comes from [1].
    References
    ----------
    .. [1] Landesfeind, J. and Gasteiger, H.A., 2019. Temperature and Concentration
    Dependence of the Ionic Transport Properties of Lithium-Ion Battery Electrolytes.
    Journal of The Electrochemical Society, 166(14), pp.A3079-A3097.
    ----------
    c_e: :class:`pybamm.Symbol`
        Dimensional electrolyte concentration
    T: :class:`pybamm.Symbol`
        Dimensional temperature
    coeffs: :class:`pybamm.Symbol`
        Fitting parameter coefficients
    Returns
    -------
    :class:`pybamm.Symbol`
        Electrolyte transference number
    """
    c = c_e / 1000  # mol.m-3 -> mol.l
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = coeffs
    tplus = (
        p1
        + p2 * c
        + p3 * T
        + p4 * c ** 2
        + p5 * c * T
        + p6 * T ** 2
        + p7 * c ** 3
        + p8 * c ** 2 * T
        + p9 * c * T ** 2
    )

    return tplus
