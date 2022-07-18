import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from src.metric import Metric


def draw_learning_curve(k, metrics: list[Metric]):
    fig = make_subplots(1, k)

    for i, metric in enumerate(metrics, 1):
        title = f"FOLD {metric.fold}"
        epoch = np.arange(len(metric.train_loss_rmse))

        fig.add_trace(
            go.Scatter(
                x=epoch,
                y=np.array(metric.train_loss_rmse),
                mode="lines+markers",
                name=f"train_loss(fold:{metric.fold})",
                line=dict(color="blue"),
            ),
            1,
            i,
        )

        fig.add_trace(
            go.Scatter(
                x=epoch,
                y=np.array(metric.valid_loss_rmse),
                mode="lines+markers",
                name=f"valid_loss(fold:{metric.fold})",
                line=dict(color="orange"),
            ),
            1,
            i,
        )

    fig.write_image(f"figures/learning.png")
