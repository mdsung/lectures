from dataclasses import dataclass

import torch
import torch.nn as nn


@dataclass
class Metric:
    fold: int
    train_loss_rmse: float
    valid_loss_rmse: float


def log_rmse(pred_y, labels):
    clipped_preds = torch.clamp(pred_y, 1, float("inf"))
    rmse = torch.sqrt(nn.MSELoss()(torch.log(clipped_preds), torch.log(labels)))
    return rmse.item()
