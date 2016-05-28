# Copyright (c) 2014, German Neuroinformatics Node (G-Node)
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted under the terms of the BSD License. See
# LICENSE file in the root of the Project.

from __future__ import (absolute_import, division, print_function)#, unicode_literals)

try:
    import nixio.core as ccore
    from nixio.core import LinkType, Source, Section
except ImportError:
    ccore = None
    # TODO: The following will be replaced by Python classes
    LinkType = None
    Source = None
    Section = None

from nixio.pycore.file import File, FileMode
from nixio.value import Value, DataType
from nixio.pycore.dimensions import DimensionType

from nixio.block import BlockMixin
from nixio.file import FileMixin
from nixio.section import SectionMixin
from nixio.value import Value, DataType
from nixio.property import PropertyMixin
from nixio.source import SourceMixin
from nixio.data_array import DataSetMixin
from nixio.data_array import DataArrayMixin
from nixio.tag import TagMixin
from nixio.multi_tag import MultiTagMixin
from nixio.group import GroupMixin
from nixio.entity_with_sources import (DataArraySourcesMixin,
                                       MultiTagSourcesMixin, TagSourcesMixin)

from nixio.section import S

__all__ = ("File", "FileMode", "DataType", "Value", "LinkType", "DimensionType")

del (BlockMixin, FileMixin, SectionMixin, PropertyMixin, SourceMixin,
     DataArrayMixin, TagMixin)
del (MultiTagMixin, DataArraySourcesMixin, MultiTagSourcesMixin,
     TagSourcesMixin, GroupMixin)

__author__ = ('Christian Kellner, Adrian Stoewer, Andrey Sobolev, Jan Grewe,'
              ' Balint Morvai')
