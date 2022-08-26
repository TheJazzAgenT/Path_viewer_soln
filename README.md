# Path_viewer_hw
## Installation
### Requirements
* Python 3.X

### Installing Dependencies in a virtual environment
Clone the repo
```
$ pip install --upgrade virtualenv
$ virtualenv env
$ source env/Scripts/activate
$ pip install -r requirements.txt
```
## Running
`python main.py --stl_file /path/to/part.stl --csv_file /path/to/cut_path.csv --cut_color red`

To view multiple stl files and cut paths at once, simply add another `--stl_file` and `--csv_file` argument.

**Arguments:**


* stl_file
    The path to a single .stl file on disk.
    Multiple of this argument can be provided.


* csv_file
    The path to a single .csv file on disk, representing the cut path to view.
    Multiple of this argument can be provided.


* cut_color (optional)
    The color to display your cut path in.
    Multiple of this argument can be provided.
    Colors will be applied in order to csv files.
    Any [matplotlib default color](https://matplotlib.org/stable/gallery/color/named_colors.html) is acceptable.
