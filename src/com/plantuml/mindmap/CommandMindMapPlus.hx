package com.plantuml.mindmap;

import com.plantuml.core.Diagram;
import com.plantuml.command.*;
import com.plantuml.command.regex.*;

class CommandMindMapPlus extends SingleLineCommand {
	public function new() {
		_init([
			RegexLeaf.start(), //
			new RegexLeaf(1, "([+-]+)", "TYPE"), //
			new RegexOptional(new RegexLeaf(1, "\\[(#\\w+)\\]", "BACKCOLOR")), //
			new RegexLeaf(1, "(_)?", "SHAPE"), //
			RegexLeaf.spaceOneOrMore(), //
			new RegexLeaf(1, "([^%s].*)", "LABEL"),
			RegexLeaf.end()
		]);
	}

	public function executeArg(diagram:Diagram, lines:BlocLines, map:Map<String, String>):CommandExecutionResult {
		throw new haxe.exceptions.NotImplementedException();
	}
}
