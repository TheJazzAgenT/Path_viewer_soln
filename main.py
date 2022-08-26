import click
import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

from cut_path import CutPath
from point import Point


@click.command(context_settings=dict(ignore_unknown_options=True))
@click.option('--csv_file', help='path to csv file on disk', multiple=True)
@click.option('--stl_file', help='path to csv file on disk', multiple=True)
def run(csv_file, stl_file):
    if len(csv_file) != len(stl_file):
        raise Exception("ERROR: Number of cut paths does not match the number of stls")
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)
    for csv_f, stl_f in zip(csv_file, stl_file):
        test_stl = mesh.Mesh.from_file(stl_f)
        scale = test_stl.points.flatten()

        cut_path = CutPath(csv_f)
        cut_scale = max(scale) - min(scale)
        cut_path.set_scale(cut_scale)

        axes.add_collection3d(mplot3d.art3d.Poly3DCollection(test_stl.vectors))
        axes.plot3D(cut_path.get_coords('x'), cut_path.get_coords('y'), cut_path.get_coords('z'), color='red', linewidth=3)
        axes.auto_scale_xyz(scale, scale, scale)

    pyplot.show()

if __name__=='__main__':
    run()
