package com.plantuml.mindmap;

import com.plantuml.command.*;
import com.plantuml.command.regex.*;
import com.plantuml.core.Diagram;

class CommandMindMapDirection extends SingleLineCommand {
	public function new() {
		_init([
			RegexLeaf.start(),
			new RegexLeaf(0, "[^*]*"), //
			new RegexLeaf(0, "\\b"), //
			new RegexLeaf(1, "(left|right)", "DIRECTION"), //
			new RegexLeaf(0, "\\b"), //
			new RegexLeaf(0, "[^*]*"),
			RegexLeaf.end()
		]);
	}

	public function executeArg(diagram:Diagram, lines:BlocLines, map:Map<String, String>):CommandExecutionResult {
		throw new haxe.exceptions.NotImplementedException();
	}
}
