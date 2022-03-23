package com.plantuml.command;

import com.plantuml.core.Diagram;
import com.plantuml.command.*;
import com.plantuml.command.regex.*;

abstract class CommandMultilines2 implements Command {
	final patternStart:IRegex;

	public function new(patternStart:IRegex) {
		this.patternStart = patternStart;
	}
}
