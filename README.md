# Waymo LiDAR SLAM + Driving Decision Project

This repository contains a starter implementation for an autonomy-style project built around the Waymo Open Dataset.

## Project goals

- Build a LiDAR SLAM pipeline on the Waymo Perception dataset
- Produce ego-pose estimates and local maps
- Train a driving decision / future trajectory model on top of scene state
- Keep the code modular and research-friendly

## Planned modules

- `src/data/`: dataset loading and parsing
- `src/slam/`: LiDAR odometry, submaps, pose graph, mapping
- `src/planning/`: scene encoding and driving decision model
- `src/utils/`: shared helpers
- `configs/`: YAML config files
- `scripts/`: entry-point scripts

## First milestone

1. Parse Waymo data into usable point clouds / scene tensors
2. Run a lightweight LiDAR odometry baseline
3. Save trajectories and maps
4. Train a simple future trajectory predictor

## Status

This is the initial scaffold. The current version includes:

- project folder layout
- placeholder config files
- Python package structure
- starter scripts
- baseline interfaces for SLAM and planning

## Suggested setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Notes

The full Waymo Open Dataset is not included in this repository. You will need to download the relevant dataset splits separately.
