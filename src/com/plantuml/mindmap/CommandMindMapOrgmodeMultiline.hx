package com.plantuml.mindmap;

import com.plantuml.command.*;
import com.plantuml.command.CommandControl;
import com.plantuml.command.CommandExecutionResult;
import com.plantuml.command.CommandMultilines2;
import com.plantuml.command.regex.*;
import com.plantuml.command.regex.RegexConcat;
import com.plantuml.core.Diagram;

class CommandMindMapOrgmodeMultiline extends CommandMultilines2 {
	public function new() {
		// _init([
		// 	RegexLeaf.start(), //
		// 	new RegexLeaf(1, "(0)", "TYPE"), //
		// 	RegexLeaf.spaceOneOrMore(), //
		// 	new RegexLeaf(1, "([^%s].*)", "LABEL"),
		// 	RegexLeaf.end()
		// ]);

		final start = new RegexConcat([
			RegexLeaf.start(), //
			new RegexLeaf(1, "([*]+)", "TYPE"), //
			new RegexOptional(new RegexLeaf(1, "\\[(#\\w+)\\]", "BACKCOLOR")), //
			new RegexLeaf(1, "(_)?", "SHAPE"), //
			new RegexLeaf(0, ":"), //
			new RegexLeaf(1, "(.*)", "DATA"), //
			RegexLeaf.end()
		]);

		super(start);
	}

	public function isValid(lines:BlocLines):CommandControl {
		throw new haxe.exceptions.NotImplementedException();
	}

	public function execute(diagram:Diagram, lines:BlocLines):CommandExecutionResult {
		throw new haxe.exceptions.NotImplementedException();
	}
}
