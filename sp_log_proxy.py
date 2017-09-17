#!/usr/local/bin/python2.7
# encoding: utf-8
'''
sp.sp_log_proxy -- single paticle log converter

It defines classes_and_methods that process MotionCor2 log and make it can be read by motioncorr log viewer

@author:     xiaodong han

@copyright:  2017 bluejayimaging. All rights reserved.

@license:    GPLv2

@contact:    xiaodong.han@bluejayimaging.com
@deffield    updated: Updated
'''

import sys
import os
import getopt

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

__all__ = []
__version__ = 0.1
__date__ = '2017-09-16'
__updated__ = '2017-09-17'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by xiaodong han on %s.

  Copyright (C) 1989, 1991 Free Software Foundation, Inc., <http://fsf.org/>
  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
  Everyone is permitted to copy and distribute verbatim copies
  of this license document, but changing it is not allowed.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-r", "--recursive", dest="recurse", action="store_true", help="recurse into subfolders [default: %(default)s]")
        parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
        parser.add_argument("-i", "--include", dest="include", help="only include paths matching this regex pattern. Note: exclude is given preference over include. [default: %(default)s]", metavar="RE" )
        parser.add_argument("-e", "--exclude", dest="exclude", help="exclude paths matching this regex pattern. [default: %(default)s]", metavar="RE" )
        parser.add_argument('-V', '--version', action='version', version=program_version_message)
        parser.add_argument(dest="paths", help="paths to folder(s) with source file(s) [default: %(default)s]", metavar="path", nargs='+')

        # Process arguments
        print argv
        argv = argv[1:]
        optlist, args = getopt.getopt(argv, 'hrvieV', ['input=', 'output='])
        print optlist,args

        verbose = False
        recurse = False
        inpat = False
        expat = False
        input_file = ''
        output_file = ''
        for o in optlist:
            #print o[0]
            #print o[1]
            if o[0] == '-v':
                verbose = True
            elif o[0] == '-r':
                recurse = True
            elif o[0] == '-i':
                inpat = True
            elif o[0] == '-e':
                expat = True
            elif o[0] == '--input':
                input_file = o[1]
            elif o[0] == '--output':
                output_file = o[1]

        if verbose:
            print("Verbose mode on")
            if recurse:
                print("Recursive mode on")
            else:
                print("Recursive mode off")

        if inpat and expat and inpat == expat:
            raise CLIError("include and exclude pattern are equal! Nothing will be processed.")

        # check if input file exist
        cwd = os.getcwd()
        print 'cwd: ' + cwd
        if os.path.isfile(input_file):
            # read file
            print 'input file exist'
            fr = open(input_file, 'r')
            fw = open(output_file, 'w')
            try:
                lines = fr.readlines()
                for line in lines:
                    print line
                    # remove space at the beginning of the line
                    line = ' '.join(line.split())
                    if line.startswith('#') is True:
                        line = line + '\n'
                    else:
                        number = line.split()[0]
                        # format number to 3 bits
                        number = '%03d' %int(number)
                        number = '#' + number + ' :'

                        line = line.split()[1:]
                        line.insert(0, number)
                        line = ' '.join(line)
                        line = '......Shift of Frame ' + line + '\n'
                    fw.write(line)
            finally:
                fr.close()
                fw.close()

        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception, e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-h")
        sys.argv.append("-v")
        sys.argv.append("-r")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'sp.sp_log_proxy_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())