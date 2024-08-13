data_file = string()
parameters_file = string()
sed_modules = cigale_string_list()
analysis_method = string()
cores = integer(min=1)
bands = cigale_string_list()
properties = cigale_string_list()
additionalerror = float(min=0.0)
[sed_modules_params]
  [[sfhdelayed]]
    tau_main = cigale_list()
    age_main = cigale_list(dtype=int, minvalue=0.)
    tau_burst = cigale_list()
    age_burst = cigale_list(dtype=int, minvalue=1.)
    f_burst = cigale_list(minvalue=0., maxvalue=0.9999)
    sfr_A = cigale_list(minvalue=0.)
    normalise = boolean()
  [[bc03]]
    imf = cigale_list(dtype=int, options=0. & 1.)
    metallicity = cigale_list(options=0.0001 & 0.0004 & 0.004 & 0.008 & 0.02 & 0.05)
    separation_age = cigale_list(dtype=int, minvalue=0)
  [[dustatt_modified_starburst]]
    E_BV_lines = cigale_list(minvalue=0.)
    E_BV_factor = cigale_list(minvalue=0., maxvalue=1.)
    uv_bump_wavelength = cigale_list(minvalue=0.)
    uv_bump_width = cigale_list()
    uv_bump_amplitude = cigale_list(minvalue=0.)
    powerlaw_slope = cigale_list()
    Ext_law_emission_lines = cigale_list(dtype=int, options=1 & 2 & 3)
    Rv = cigale_list()
    filters = string()
  [[redshifting]]
    redshift = cigale_list(minvalue=0.)
[analysis_params]
  variables = cigale_string_list()
  bands = cigale_string_list()
  save_best_sed = boolean()
  save_chi2 = option('all', 'none', 'properties', 'fluxes')
  lim_flag = option('full', 'noscaling', 'none')
  mock_flag = boolean()
  redshift_decimals = integer()
  blocks = integer(min=1)
