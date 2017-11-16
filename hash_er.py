#!/usr/bin/python
"""
Hasher Module:
This module is designed to handle any kind of hashing a user may need to use.

Author: Sunrise Cobb
"""


import hashlib


def HashString(string, algorithm):
  """
  This function hashes any string. Supported algorithms are: ['sha1', 'sha224', 'sha384', 'sha256', 'sha512', 'md5']

  Args: string, aglorithm
  Returns: string
  """

  # set up the syntax string with our vars
  hash_syntax = 'hashlib.%s(b\'%s\')' % (algorithm, string)
  hash_object = eval(hash_syntax)
  hex_dig = hash_object.hexdigest()

  return hex_dig


def HashFile(filename, algorithm):
  """
  This function hashes any file. Supported algorithms are: ['sha1', 'sha224', 'sha384', 'sha256', 'sha512', 'md5']

  Args: filename, aglorithm
  Returns: string
  """

  # set how many blocks we want to read in at a time
  blocksize = 65536

  # set up the syntax with our vars
  hash_syntax = 'hashlib.%s()' % algorithm
  hash_object = eval(hash_syntax)

  # now lets go ahead and create the hash for the file
  with open(filename, 'rb') as afile:
    buf = afile.read(blocksize)
    while len(buf) > 0:
      hash_object.update(buf)
      buf = afile.read(blocksize)

  hex_dig = hash_object.hexdigest()

  return hex_dig