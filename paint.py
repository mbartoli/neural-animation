#!/usr/bin/python
__author__ = 'mbartoli'

import argparse
import subprocess
import sys
import os
import errno
import time


def make_sure_path_exists(path):
    '''
    make sure input and output directory exist, if not create them.
    If another error (permission denied) throw an error.
    '''
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def main(input, output, style, start_frame, end_frame):
    make_sure_path_exists(input)
    make_sure_path_exists(output)

    nrframes =len([name for name in os.listdir(input) if os.path.isfile(os.path.join(input, name))])
    if nrframes == 0:
        print("no frames to process found")
        sys.exit(0)

    if start_frame is None:
     	frame_i = 1
    else:
	frame_i = int(start_frame)
    if not end_frame is None:
    	nrframes = int(end_frame)+1
    else:
	nrframes = nrframes+1

    now = time.time()
    totaltime = 0

    for i in xrange(frame_i, nrframes):
        print('Processing frame #{}').format(frame_i)

	os.system("th neural_style.lua -num_iterations 2000 -style_image " + style + " -content_image " + input + "/%08d.jpg" % frame_i + " -print_iter 2000 -output_image " + output + "/%08d.jpg" % frame_i)	
	
   	later = time.time()
   	difference = int(later - now)
	totaltime += difference
	avgtime = (totaltime / i)

	print '***************************************'
	print 'Saving Image As: ' + output +"/%08d.jpg" % frame_i
	print 'Frame ' + str(i) + ' of ' + str(nrframes-1)
	print 'Frame Time: ' + str(difference) + 's'
	timeleft = avgtime * ((nrframes-1) - frame_i)        
	m, s = divmod(timeleft, 60)
	h, m = divmod(m, 60)
	print 'Estimated Total Time Remaining: ' + str(timeleft) + 's (' + "%d:%02d:%02d" % (h, m, s) + ')'
	print '***************************************'

        now = time.time()
        frame_i += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Implementing neural art on video.')
    parser.add_argument(
        '-i','--input',
        help='Input directory where extracted frames are stored',
        required=True)
    parser.add_argument(
        '-o','--output',
        help='Output directory where processed frames are to be stored',
        required=True)
    parser.add_argument(
	'-s','--style',
	help='Image to base the style after',
	required=True)
    parser.add_argument(
    	'-sf', '--start_frame',
        type=int,
    	required=False,
    	help="starting frame nr")
    parser.add_argument(
    	'-ef', '--end_frame',
        type=int,
    	required=False,
    	help="end frame nr")

    args = parser.parse_args()

    main(args.input, args.output, args.style, args.start_frame, args.end_frame)
