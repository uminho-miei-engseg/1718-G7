# coding: latin-1
###############################################################################
# eVotUM - Electronic Voting System
#
# generateBlindData-app.py
#
# Cripto-7.1.1 - Commmad line app to exemplify the usage of blindData
#       function (see eccblind.py)
#
# Copyright (c) 2016 Universidade do Minho
# Developed by André Baptista - Devise Futures, Lda. (andre.baptista@devisefutures.com)
# Reviewed by Ricardo Barroso - Devise Futures, Lda. (ricardo.barroso@devisefutures.com)
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
###############################################################################
"""
Command line app that receives Data and pRDashComponents from STDIN and writes
blindMessage and blindComponents and pRComponents to STDOUT.
"""
from eVotUM.Cripto import utils
import sys
from eVotUM.Cripto import eccblind


def printUsage():
    print("Usage: python blindSignature-app.py -key \"private key\" -bmsg \"blind message\"")

def parseArgs():
    if (len(sys.argv) == 5 and sys.argv[1] == '-key' and sys.argv[3] == '-bmsg'):
        pemKey = utils.readFile(sys.argv[2])
        with open('assinante.txt','r') as out:
            initComponents = out.readline().rstrip()
        passphrase = raw_input("Passphrase: ")
        errorCode, blindSignature = eccblind.generateBlindSignature(pemKey, passphrase, sys.argv[4], initComponents)
        showResults(errorCode,blindSignature)
    else:
        printUsage()

def showResults(errorCode, result):
    print("Output")
    if (errorCode is None):
        print("Blind Signature: %s" % result)
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")

if __name__ == "__main__":
    parseArgs()
