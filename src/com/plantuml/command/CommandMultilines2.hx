package com.plantuml.command;

import com.plantuml.core.Diagram;
import com.plantuml.command.*;
import com.plantuml.command.regex.*;

abstract class CommandMultilines2 implements Command {
	final regexStart:IRegex;

	public function new(regexStart:IRegex) {
		this.regexStart = regexStart;
	}

	public function isValid(lines:BlocLines):CommandControl {
		final s = lines.getFirst();
		if (regexStart.match(s) == false)
			return CommandControl.NOT_OK;

		throw new haxe.exceptions.NotImplementedException();
	}
}
