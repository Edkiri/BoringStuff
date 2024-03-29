#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to Europan DD-MM-YYY.

import shutil, os, re

# Create a regex that match files with the American date format.
datePattern = re.compile(r"""
  ^(.*?)          # all text before the date
  ((0|1)?\d)-     # one or two digits for the month
  ((0|1|2|3)?\d)- # one or two digits for the day
  ((19|20)\d\d)   # for digits for the year
  (.*?)$
""", re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
  mo = datePattern.search(amerFilename)

  if mo == None:
    continue

  # Get the different parts of the filename.
  beforePart = mo.group(1)
  monthPart  = mo.group(2)
  dayPart    = mo.group(4)
  yearPart   = mo.group(6)
  afterPart  = mo.group(8)


  # Form the Europan-style filename.
  euroFilename = beforePart + '-' + dayPart + '-' + monthPart + '-' + yearPart + afterPart

  # Get the full, absolute file paths.
  absWorkingDir = os.path.abspath('.')
  amerFilename = os.path.join(absWorkingDir, amerFilename)
  euroFilename = os.path.join(absWorkingDir, euroFilename)

  # Rename the files.
  print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
  shutil.move(amerFilename, euroFilename)
