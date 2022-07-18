from src.drawer import draw_learning_curve
from src.metric import Metric


def test_draw_learning_curve():
    metrics = [
        Metric(0, [3, 2, 1], [2.9, 2.2, 1.5]),
        Metric(1, [3, 2, 1], [2.9, 2.2, 1.5]),
    ]
    draw_learning_curve(metrics)
    assert 0
