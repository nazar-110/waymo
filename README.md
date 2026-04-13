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

## First runnable milestone

1. Run a synthetic LiDAR sequence through the SLAM frontend
2. Produce and visualize an estimated trajectory
3. Keep the planning model stub ready for future trajectory prediction
4. Extend the data layer to real Waymo TFRecords next

## Current repo contents

- lightweight project structure
- synthetic LiDAR dataset for development without Waymo files
- ICP-based LiDAR odometry baseline using Open3D
- runnable SLAM demo script
- starter planning model in PyTorch

## Suggested setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_slam.py
```

## Notes

The full Waymo Open Dataset is not included in this repository. You will need to download the relevant dataset splits separately.
