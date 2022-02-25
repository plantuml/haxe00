package com.plantuml.command;

import com.plantuml.core.Diagram;

interface Command {
	public function isValid(lines:BlocLines):CommandControl;

	public function execute(diagram:Diagram, lines:BlocLines):CommandExecutionResult;
}
