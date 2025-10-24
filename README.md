# Fourier approximation of magMEMS oscillations: neural network space handling

The repository explores Fourier-based approximations and neural-network–assisted residual minimization for periodic solutions of a conservative magMEMS oscillator, and studies dynamic pull‑in thresholds as a function of geometry.

## What’s here
- `main_no_xi.ipynb` — Fourier/NN workflow for the limiting case ξ → 0.
- `main_with_xi.ipynb` — General case with nonzero ξ and parameter studies.
- `plot_KstarAstar.py` — Reproduces the K* (pull‑in threshold) and A* (max deflection) curves; saves figures to `figs/`.
- `network_diagram.py` — Visualizes the neural model architecture.
- `data/` — Normalization parameters and precomputed θ-grids used by notebooks.
- `saved_models/` — Pretrained `.pt` checkpoints and model params.

## Quick start
1) Python 3.10+ recommended. Install dependencies: `pip install -r requirements.txt`
2) Open and run `main_no_xi.ipynb` or `main_with_xi.ipynb` to reproduce the analyses.
3) To regenerate the K*/A* plot, run `plot_KstarAstar.py` (outputs to `figs/`).

## Citation
If you use this code, please cite the manuscript:

“Fourier approximation of magMEMS oscillations: neural network space handling,” submitted to Micromachines (MDPI), 2025.

