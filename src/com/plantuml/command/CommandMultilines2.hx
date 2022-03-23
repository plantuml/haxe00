package com.plantuml.command;

import com.plantuml.core.Diagram;
import com.plantuml.command.*;
import com.plantuml.command.regex.*;

abstract class CommandMultilines2 implements Command {
	final regexStart:IRegex;
	final regexEnd:IRegex;

	public function new(regexStart:IRegex, regexEnd:IRegex) {
		this.regexStart = regexStart;
		this.regexEnd = regexEnd;
	}

	public function isValid(lines:BlocLines):CommandControl {
		trace('lines=$lines');
		final s = lines.getFirst();
		if (regexStart.match(s) == false)
			return CommandControl.NOT_OK;

		if (lines.size() == 1)
			return CommandControl.OK_PARTIAL;

		if (regexEnd.match(lines.getLast()))
			return CommandControl.OK;

		return CommandControl.OK_PARTIAL;
	}
}
