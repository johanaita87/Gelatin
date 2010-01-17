# Copyright (C) 2010 Samuel Abels.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
from Gelatin import INDENT
from Token   import Token

class MatchStatement(Token):
    def __init__(self):
        self.matchlist  = None
        self.statements = None

    def parse(self, context):
        match = self.matchlist.match(context)
        if not match:
            return 0
        context.re_stack.append(match)
        for statement in self.statements:
            statement.parse(context)
        context.re_stack.pop()
        return 1

    def dump(self, indent = 0):
        res  = INDENT * indent + 'match:\n'
        res += self.matchlist.dump(indent + 1)
        for statement in self.statements:
            res += statement.dump(indent + 2) + '\n'
        return res