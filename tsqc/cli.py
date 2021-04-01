
import argparse


def _cli_parser():
    """Reads command line arguments and returns input specifications"""
    parser = argparse.ArgumentParser()
    parser.add_argument("input_files", nargs="+", type=str,
                        help="One or more tab-delimited timeseries files. Can "
                             "also be a single string with a wildcard (*) to "
                             "specify all files matching the file pattern. If "
                             "so, these files are naturally sorted by file name "
                             "prior to extraction")
    parser.add_argument("confounds_files", type=str,
                        help="One or more tab-delimited confounds file. Can "
                             "also be a single string with a wildcard (*) to "
                             "specify all files matching the file pattern. If "
                             "so, these files are naturally sorted by file name "
                             "prior to extraction. Each column should contain a "
                             "confound timeseries, and the first row should be "
                             "the confound name (i.e. column header). REQUIRED "
                             "CONFOUNDS: 6 head motion parameters 'trans_x', "
                             "'trans_y' 'trans_z', 'rot_x', 'rot_y', 'rot_z'; "
                             "Framewise displacement 'framewise_displacement'; "
                             "DVARS `dvars`")
    parser.add_argument("out_dir", type=str,
                        help="The path to the output directory. Created if it"
                             "does not already exist")
    parser.add_argument("-a", "--atlas", type=str,
                        help="Atlas used to compute distances between regions "
                             "in the timeseries. Can either be 1) a volumetric "
                             "NIfTI image or 2) a tab-delimited coordinate file. "
                             "If a NIfTI image, then region labels should be "
                             "in the same order as the timeseries (i.e. region "
                             "1 should be column 1). If a .tsv file, must "
                             "include columns 'x', 'y', 'z' (other columns will "
                             "be ignored), with each region as a row. Rows must "
                             "be in the same order as the timeseries file "
                             "(i.e. row 1 must be column 1 of the timeseries)")
    return parser.parse_args()