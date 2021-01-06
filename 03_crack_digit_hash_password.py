#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i", "--input", dest="input", help="Input Hash File Path")
    parser.add_option("-o", "--output", dest="output", help="Insert Output File Path")
    parser.add_option("-h", "--hashtype", dest="output", help="Insert Hash Type (hashcat mode)")
    (options, arguments)=parser.parse_args()
    if not options.input:
        parser.error("[-] Please specify an input file path, use --help for more info.")
    elif not options.output:
        parser.error("[-] Please specify an output file path, use --help for more info.")
    elif not options.hashtype:
        parser.error("[-] Please specify an hashcat hash type (Mode), use --help for more info.")
    return options

def runHashcat(input, output, hashtype):
    subprocess.call('hashcat -a 3 -m '+hashtype+' --username -o '+output+' '+input+' -1 ?d ?1?1?1?1?1?1?1?1?1?1?1 --increment --increment-min 3', shell=True)
    

options=get_arguments()
runHashcat(options.input, options.output, options.hashtype )