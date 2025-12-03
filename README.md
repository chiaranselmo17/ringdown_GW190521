# ringdown_GW190521

This repository accompanies
**_Black-hole ringdown with templates capturing spin precession: a critical re-analysis of GW190521_**,  
by *Chiara Anselmo, Costantino Pacilio, and Davide Gerosa*, XXX.

It provides the posterior samples used to generate the figures and results in the paper.

---

## Credits

You are welcome to use these data in your research.  
If you do so, **please cite the paper above**.

If you download and directly use files from this release, **also cite the dataset DOI: XXX**.

---

## Data

The full dataset is ~95 MB.  
You can download all files from the GitHub release page or by using the included script:

```bash
python download.py
```

Data files are provided in `.npy` (NumPy arrays).

---

## Dataset Structure

Each file in this release follows the naming pattern:

*[GPR_mean / GPR_random]_[binary_parameters / mode_amplitudes]_[aligned / precessing]_[6ms / 12ms][optional: _reweighted].npy*

Below is a detailed explanation of each component.


## 1. GPR options

### *GPR_mean_\**
  Posterior samples obtained using GPR mean predictions for the remnant mass and spin and for the QNM amplitudes.  
  Used to generate Figures 1-2 in the main text.

### *GPR_random_\**
  Posterior samples obtained by sampling from the full GPR predictive distributions, propagating the GPR uncertainties.  
  Used to generate Figures 4-5 in Appendix D.


## 2. Parameter sets and models

### *binary_parameters_\**
  Posterior samples for:
  - Common binary parameters:  
  `{d_L, cos(iota), M, q}`
  - Spin parameters:  
    - ***aligned*** model: `{chi_1z, chi_2z}`
    - ***precessing*** model: `{chi_1, cos(gamma_1), phi_1, chi_2, cos(gamma_2), phi_2}`
  - Mode phases:  
  `{phi_{220}, phi_{330}, phi_{210}, phi_{2-20}, phi_{3-30}, phi_{2-10}}`

### *mode_amplitudes_\**
  Posterior samples for:
  - ***aligned*** model: `{A_220, A_330, A_210}`
  - ***precessing*** model: `{A_{2±2,0}, A_{3±3,0}, A_{2±1,0}}`

Note: Some of these parameters were combined or omitted when producing figures.


## 3. Ringdown start times

The suffix indicates the ringdown start time used in the inference, either ***6 ms*** or ***12 ms*** after the strain peak.


## 4. Reweighted samples

Some files include an additional suffix:

***_reweighted***

This indicates that the posterior samples were reweighted following Appendix B of the paper.

**The reweighted samples are the ones shown in all figures.**
Non-reweighted samples are included for completeness.

---

Example: `mean_GPR_binary_parameters_precessing_6ms_reweighted.npy`  
This file contains GPR mean predictions, precessing model, 6 ms start time, reweighted samples.
