# ILua
# Copyright (C) 2018  guysv

# This file is part of ILua which is released under GPLv2.
# See file LICENSE or go to https://www.gnu.org/licenses/gpl-2.0.txt
# for full license details.

import os
from jupyter_console.app import ZMQTerminalIPythonApp

from .app import ILuaApp

class ILuaConsoleApp(ILuaApp):
    def run(self):
        cli_args = vars(self.parser.parse_args())

        os.environ.update({
            self.ENV_VAR_PREFIX + key.upper(): cli_args[key]
            for key in cli_args
        })

        # HACK: passing arguments to jupyter_console via command line
        #       because I have yet to figure out how to do it through
        #       IPython's fancy traitlets framework
        ZMQTerminalIPythonApp.launch_instance(argv=['--kernel', 'lua'])

def main():
    ILuaConsoleApp().run()

if __name__ == '__main__':
    main()