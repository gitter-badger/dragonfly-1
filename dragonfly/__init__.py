#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it 
#   under the terms of the GNU Lesser General Public License as published 
#   by the Free Software Foundation, either version 3 of the License, or 
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but 
#   WITHOUT ANY WARRANTY; without even the implied warranty of 
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public 
#   License along with Dragonfly.  If not, see 
#   <http://www.gnu.org/licenses/>.
#

#---------------------------------------------------------------------------
from .config            import Config, Section, Item
from .error             import DragonflyError

#---------------------------------------------------------------------------
from .engines           import get_engine, EngineError, MimicFailure

#---------------------------------------------------------------------------
from .grammar.grammar_base       import Grammar

import sys
if sys.platform.startswith("win"):
    from .grammar.grammar_connection import ConnectionGrammar
else:
    from .os_dependent_mock import ConnectionGrammar
from .grammar.rule_base          import Rule
from .grammar.rule_compound      import CompoundRule
from .grammar.rule_mapping       import MappingRule
from .grammar.elements  import (ElementBase, Sequence, Alternative,
                                Optional, Repetition, Literal,
                                ListRef, DictListRef, Dictation,
                                RuleRef, Empty, Compound, Choice)
from .grammar.context   import Context, AppContext
from .grammar.list      import ListBase, List, DictList
from .grammar.recobs    import (RecognitionObserver, RecognitionHistory,
                                PlaybackHistory)

#from .grammar.number    import (Integer, IntegerRef, Digits, DigitsRef,
#                                Number, NumberRef)

#---------------------------------------------------------------------------
from .actions           import (ActionBase, DynStrActionBase, ActionError,
                                Repeat, Key, Text, Mouse, Paste, Pause,
                                Mimic, Playback, WaitWindow, FocusWindow,
                                Function, StartApp, BringApp, PlaySound)

if sys.platform.startswith("win"):
    from .actions.keyboard  import Typeable, Keyboard
    from .actions.typeables import typeables
    from .actions.sendinput import (KeyboardInput, MouseInput, HardwareInput,
                                    make_input_array, send_input_array)
else:
    from .os_dependent_mock    import Typeable, Keyboard
    from .os_dependent_mock import typeables
    from .os_dependent_mock    import (KeyboardInput, MouseInput, HardwareInput,
                                       make_input_array, send_input_array)

#---------------------------------------------------------------------------

# OS agnostic imports
from .windows.rectangle import Rectangle, unit
from .windows.point     import Point

# Windows-specific
if sys.platform.startswith("win"):
    from .windows             import Window
    from .windows             import Monitor, monitors
    from .windows             import Clipboard
else:  # Mock imports
    from .os_dependent_mock   import Window
    from .os_dependent_mock   import Monitor, monitors
    from .os_dependent_mock   import Clipboard


#---------------------------------------------------------------------------
from .language          import (Integer, IntegerRef,
                                Digits, DigitsRef,
                                Number, NumberRef)
