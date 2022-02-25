package com.plantuml.mindmap;

using hx.strings.Strings;

import com.plantuml.command.*;
import com.plantuml.core.Diagram;

class MindMapDiagramFactory {
	var cmds:Array<Command>;

	public function new() {
		this.cmds = createCommands();
	}

	private function createCommands():Array<Command> {
		var cmds:Array<Command> = [];
		// CommonCommands.addCommonCommands1(cmds);

		cmds.push(new CommandMindMapOrgmode());
		// cmds.push(new CommandMindMapOrgmodeMultiline());
		cmds.push(new CommandMindMapRoot());
		cmds.push(new CommandMindMapPlus());
		cmds.push(new CommandMindMapDirection());

		return cmds;
	}

	private function getCandidate(s:String) {
		for (cmd in this.cmds) {
			if (cmd.isValid(BlocLines.single(s)) == CommandControl.OK)
				return cmd;
		}
		return null;
	}

	public function createSystem(lines:BlocLines):Diagram {
		var diagram = new MindMapDiagram();
		for (s in lines.getLines()) {
			if (s == "" || s.startsWith("@start")|| s.startsWith("@end"))
				continue;

			var cmd = getCandidate(s);
			if (cmd == null)
				throw new haxe.exceptions.NotImplementedException();

			var exec:CommandExecutionResult = cmd.execute(diagram, BlocLines.single(s));

			// if (exec != CommandExecutionResult.OK)
		}
		return diagram;
	}
}
