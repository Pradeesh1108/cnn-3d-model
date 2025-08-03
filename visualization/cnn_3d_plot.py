import numpy as np
import plotly.graph_objects as go


def plot_3d_activations(activations):
    surfaces = []

    for idx, activation in enumerate(activations):
        # Only process 4D outputs: (1, h, w, c)
        if activation.ndim == 4:
            activation = activation[0]  # Remove batch dimension
            h, w, c = activation.shape

            for i in range(min(c, 6)):  # Limit number of channels
                img = activation[:, :, i]
                x, y = np.meshgrid(np.arange(w), np.arange(h))

                z = np.full_like(img, fill_value=idx * 10 + i * 2, dtype=float)  # z as 2D constant array

                surfaces.append(go.Surface(
                    z=z,
                    surfacecolor=img,
                    x=x,
                    y=y,
                    colorscale='Viridis',
                    showscale=False,
                    opacity=0.8
                ))

    fig = go.Figure(data=surfaces)
    fig.update_layout(
        title="3D CNN Layer Activations",
        scene=dict(
            xaxis_title='Width',
            yaxis_title='Height',
            zaxis_title='Layer Depth'
        ),
        height=700,
        width=900
    )
    return fig
