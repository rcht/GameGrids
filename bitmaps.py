#!/usr/bin/env python

import pickle

fh = open('bitmaps.bin', 'rb')

bitmap = pickle.load(fh)

fh.close()
