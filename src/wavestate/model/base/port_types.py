#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: © 2021 Massachusetts Institute of Technology.
# SPDX-FileCopyrightText: © 2021 Lee McCuller <mcculler@mit.edu>
# NOTICE: authors should document their contributions in concisely in NOTICE
# with details inline in source files, comments, and docstrings.
"""
"""



BGT_OPTICS_PHYSICAL       = 'BG[optical]'
BGT_OPTICS_VIRTUAL        = 'BG[Voptical]'

BGT_ELECTRONICS_PHYSICAL  = 'BG[electrical]'
BGT_ELECTRONICS_VIRTUAL   = 'GB[Velectrical]'
BGT_ELECTRONICS_GLOB      = 'BG[Gelectrical]'

BGT_MECHANICS_PHYSICAL    = 'BG[mechanical]'
BGT_MECHANICS_VIRTUAL     = 'GB[Vmechanical]'
BGT_MECHANICS_GLOB        = 'BG[Gmechanical]'

BGT_RB_MECHANICS_PHYSICAL = 'BG[mechanicalRB]'
BGT_RB_MECHANICS_VIRTUAL  = 'GB[VmechanicalRB]'
BGT_RB_MECHANICS_GLOB     = 'BG[GmechanicalRB]'

BGT_SIGNAL_OUT            = 'BG[Osignal]'
BGT_SIGNAL_IN             = 'BG[Isignal]'
BGT_SIGNAL_INOUT          = 'BG[IOsignal]'


MAX_SINGLE_BOND = [
    BGT_OPTICS_PHYSICAL,
    BGT_ELECTRONICS_PHYSICAL,
    BGT_MECHANICS_PHYSICAL,
    BGT_RB_MECHANICS_PHYSICAL,
]

ALLOWED_GLOBS = {
    BGT_ELECTRONICS_PHYSICAL : BGT_ELECTRONICS_GLOB,
    BGT_MECHANICS_PHYSICAL : BGT_MECHANICS_GLOB,
    BGT_RB_MECHANICS_PHYSICAL : BGT_RB_MECHANICS_GLOB,
}

ALLOWED_PARTNERS = {
    BGT_OPTICS_PHYSICAL : [
        BGT_OPTICS_PHYSICAL,
        BGT_OPTICS_VIRTUAL
    ],
    BGT_OPTICS_VIRTUAL : [
        BGT_OPTICS_PHYSICAL,
        BGT_OPTICS_VIRTUAL
    ],
    BGT_ELECTRONICS_PHYSICAL : [
        BGT_ELECTRONICS_GLOB,
        BGT_ELECTRONICS_PHYSICAL,
        BGT_ELECTRONICS_VIRTUAL
    ],
    BGT_ELECTRONICS_VIRTUAL : [
        BGT_ELECTRONICS_PHYSICAL,
        BGT_ELECTRONICS_VIRTUAL
    ],
    BGT_ELECTRONICS_GLOB : [
        BGT_ELECTRONICS_PHYSICAL
    ],
    BGT_MECHANICS_PHYSICAL : [
        BGT_MECHANICS_PHYSICAL,
        BGT_MECHANICS_VIRTUAL,
        BGT_MECHANICS_GLOB
    ],
    BGT_MECHANICS_VIRTUAL : [
        BGT_MECHANICS_PHYSICAL,
        BGT_MECHANICS_VIRTUAL
    ],
    BGT_MECHANICS_GLOB : [
        BGT_MECHANICS_PHYSICAL
    ],
    BGT_RB_MECHANICS_PHYSICAL : [
        BGT_RB_MECHANICS_PHYSICAL,
        BGT_RB_MECHANICS_VIRTUAL,
        BGT_RB_MECHANICS_GLOB
    ],
    BGT_RB_MECHANICS_VIRTUAL : [
        BGT_RB_MECHANICS_PHYSICAL,
        BGT_RB_MECHANICS_VIRTUAL
    ],
    BGT_RB_MECHANICS_GLOB : [
        BGT_RB_MECHANICS_PHYSICAL
    ],
    BGT_SIGNAL_OUT : [BGT_SIGNAL_IN, BGT_SIGNAL_INOUT],
    BGT_SIGNAL_IN : [BGT_SIGNAL_OUT, BGT_SIGNAL_INOUT],
    BGT_SIGNAL_INOUT: [BGT_SIGNAL_OUT, BGT_SIGNAL_IN],
}


INOUT_TYPES = [
    BGT_OPTICS_PHYSICAL,
    BGT_OPTICS_VIRTUAL,
    BGT_ELECTRONICS_PHYSICAL,
    BGT_ELECTRONICS_GLOB,
    BGT_ELECTRONICS_VIRTUAL,
    BGT_MECHANICS_PHYSICAL,
    BGT_MECHANICS_GLOB,
    BGT_MECHANICS_VIRTUAL,
    BGT_RB_MECHANICS_PHYSICAL,
    BGT_RB_MECHANICS_GLOB,
    BGT_RB_MECHANICS_VIRTUAL,
    #these are actually bidirectional, but they overload out or in linkage types
    BGT_SIGNAL_INOUT,
    BGT_SIGNAL_OUT,
    BGT_SIGNAL_IN,
]

BASIS_TYPES = {
    BGT_OPTICS_PHYSICAL       : 'optical',
    BGT_OPTICS_VIRTUAL        : 'optical',

    BGT_ELECTRONICS_PHYSICAL  : 'electrical',
    BGT_ELECTRONICS_VIRTUAL   : 'electrical',
    BGT_ELECTRONICS_GLOB      : 'electrical',

    BGT_MECHANICS_PHYSICAL    : 'mechanical',
    BGT_MECHANICS_VIRTUAL     : 'mechanical',
    BGT_MECHANICS_GLOB        : 'mechanical',

    BGT_RB_MECHANICS_PHYSICAL : 'mechanical',
    BGT_RB_MECHANICS_VIRTUAL  : 'mechanical',
    BGT_RB_MECHANICS_GLOB     : 'mechanical',

    BGT_SIGNAL_OUT            : 'signal',
    BGT_SIGNAL_IN             : 'signal',
    BGT_SIGNAL_INOUT          : 'signal',
}
