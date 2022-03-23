package com.plantuml.error;

import com.plantuml.command.BlocLines;
import com.plantuml.core.Diagram;

class PSystemErrorUtils {
	public static function syntaxErrorAt(lines:BlocLines):Diagram {
		return new DiagramSyntaxError(lines);
	}
}
