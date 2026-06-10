# Tasks

## Project Setup

- [x] Create repository structure
- [x] Add `.gitignore`
- [ ] Fill project documentation in `docs/`
- [ ] Define team roles in `docs/team.md`

## Data

- [ ] Describe dataset sources in `docs/dataset.md`
- [ ] Add sample data to `data/samples/`
- [ ] Implement dataset preparation in `scripts/prepare_dataset.py`
- [ ] Implement train/validation/test split in `scripts/split_dataset.py`
- [ ] Implement annotation conversion in `scripts/convert_annotations.py`
- [ ] Document annotation rules in `docs/annotation.md`

## Model

- [ ] Define baseline U-Net model in `ml/models/unet.py`
- [ ] Implement dataset loader in `ml/dataset.py`
- [ ] Implement training pipeline in `ml/train.py`
- [ ] Implement prediction pipeline in `ml/predict.py`
- [ ] Implement evaluation pipeline in `ml/evaluate.py`
- [ ] Configure training parameters in `configs/train_config.yaml`
- [ ] Document model approach in `docs/model.md`

## Backend

- [ ] Define API endpoints in `backend/main.py`
- [ ] Add inference endpoint
- [ ] Add health check tests
- [ ] Document backend architecture in `docs/architecture.md`

## Frontend

- [ ] Choose frontend stack
- [ ] Create frontend scaffold
- [ ] Add UI for uploading data
- [ ] Add UI for viewing prediction results

## Testing

- [ ] Add tests for data scripts
- [ ] Add tests for ML utilities
- [ ] Add tests for backend API
- [ ] Document test commands in `tests/README.md`
