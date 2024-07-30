from pathlib import Path


def init_style(app) -> None:
    with Path(__file__).parent.parent.joinpath('static').joinpath('light.css').open('r', encoding='utf-8') as f:
        style = f.read()
    app.setStyleSheet(style)
