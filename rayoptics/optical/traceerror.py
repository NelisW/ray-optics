#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2018 Michael J. Hayford
""" Support for ray trace exception handling

Created on Wed Oct 24 15:22:40 2018

@author: Michael J. Hayford
"""


class TraceError(Exception):
    """ Exception raised when ray tracing a model """


class TraceMissedSurfaceError(TraceError):
    """ Exception raised when ray misses a surface """
    def __init__(self, ifc, prev_seg):
        self.ifc = ifc
        self.prev_seg = prev_seg


class TraceTIRError(TraceError):
    """ Exception raised when ray TIRs on a surface """
    def __init__(self, ifc, int_pt, inc_dir, prev_indx, follow_indx):
        self.ifc = ifc
        self.int_pt = int_pt
        self.inc_dir = inc_dir
        self.prev_indx = prev_indx
        self.follow_indx = follow_indx


class TraceRayBlockedError(TraceError):
    """ Exception raised when ray is blocked by an aperture on a surface """
    def __init__(self, ifc, int_pt, inc_dir, prev_indx, follow_indx):
        self.ifc = ifc
        self.int_pt = int_pt
        self.inc_dir = inc_dir
        self.prev_indx = prev_indx
        self.follow_indx = follow_indx