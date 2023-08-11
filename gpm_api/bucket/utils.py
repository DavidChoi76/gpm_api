#!/usr/bin/env python3
"""
Created on Fri Jun  9 20:32:31 2023

@author: ghiggi
"""
import numpy as np
import pandas as pd


def _get_bin_edges(vmin, vmax, size):
    """Get bin edges."""
    return np.arange(vmin, vmax + 1e-10, step=size)


def _get_bin_midpoints(vmin, vmax, size):
    """Get bin midpoints."""
    edges = _get_bin_edges(vmin=vmin, vmax=vmax, size=size)
    midpoints = edges[:-1] + np.diff(edges) / 2
    return midpoints


def create_spatial_bin_empty_df(
    xbin_size=1,
    ybin_size=1,
    xlim=(-180, 180),
    ylim=(-90, 90),
    xbin_name="xbin",
    ybin_name="ybin",
):
    """Create empty spatial bin DataFrame."""

    # Get midpoints
    x_midpoints = _get_bin_midpoints(vmin=xlim[0], vmax=xlim[1], size=xbin_size)
    y_midpoints = _get_bin_midpoints(vmin=ylim[0], vmax=ylim[1], size=ybin_size)

    # Create the MultiIndex from the combination of x and y bins
    multi_index = pd.MultiIndex.from_product(
        [x_midpoints, y_midpoints], names=[xbin_name, ybin_name]
    )

    # Create an empty DataFrame with the MultiIndex
    empty_df = pd.DataFrame(index=multi_index)

    return empty_df


def add_bin_column(df, column, bin_size, vmin, vmax, bin_name, add_midpoint=True):
    # Keep rows within values
    valid_rows = df[column].between(left=vmin, right=vmax, inclusive="both")
    df = df.loc[valid_rows, :]

    # Get bin edges and midpoints
    bin_edges = _get_bin_edges(vmin=vmin, vmax=vmax, size=bin_size)
    bin_midpoints = _get_bin_midpoints(vmin=vmin, vmax=vmax, size=bin_size)

    # Get bin index
    # - 0 is outside to the left of the bins
    # - -1 is outside to the right
    # --> Subtract 1
    bin_idx = np.digitize(df[column], bins=bin_edges, right=False) - 1

    # Add bin index/midpoint values
    if add_midpoint:
        df[bin_name] = bin_midpoints[bin_idx]
    else:
        df[bin_name] = bin_idx
    return df


def add_spatial_bins(
    df,
    x="x",
    y="y",
    xbin_size=1,
    ybin_size=1,
    xlim=(-180, 180),
    ylim=(-90, 90),
    xbin_name="xbin",
    ybin_name="ybin",
    add_bin_midpoint=True,
):
    # Define x bins
    df = add_bin_column(
        df=df,
        column=x,
        bin_size=xbin_size,
        vmin=xlim[0],
        vmax=xlim[1],
        bin_name=xbin_name,
        add_midpoint=add_bin_midpoint,
    )
    # Define y bins
    df = add_bin_column(
        df=df,
        column=y,
        bin_size=ybin_size,
        vmin=ylim[0],
        vmax=ylim[1],
        bin_name=ybin_name,
        add_midpoint=add_bin_midpoint,
    )
    return df
