package com.plantuml.sequencediagram.command;

import com.plantuml.command.regex.*;
import com.plantuml.command.*;

class CommandArrow extends SingleLineCommand<SequenceDiagram> {
	public function new() {
		_init([RegexLeaf.start(), //
			RegexLeaf.end()]);
	}

	public function executeArg(diagram:SequenceDiagram, lines:BlocLines, map:Map<String, String>):CommandExecutionResult {
		throw new haxe.exceptions.NotImplementedException();
	}
}
