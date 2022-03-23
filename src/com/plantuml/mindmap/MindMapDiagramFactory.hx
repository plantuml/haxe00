package com.plantuml.mindmap;

import com.plantuml.error.PSystemErrorUtils;
import com.plantuml.command.*;
import com.plantuml.core.Diagram;
import com.plantuml.core.DiagramType;

using hx.strings.Strings;

class MindMapDiagramFactory implements PSystemFactory {
	var cmds:Array<Command>;

	public function new() {
		this.cmds = createCommands();
	}

	private function createCommands():Array<Command> {
		var cmds:Array<Command> = [];
		// CommonCommands.addCommonCommands1(cmds);

		cmds.push(new CommandMindMapOrgmode());
		cmds.push(new CommandMindMapOrgmodeMultiline());
		cmds.push(new CommandMindMapRoot());
		cmds.push(new CommandMindMapPlus());
		cmds.push(new CommandMindMapDirection());

		return cmds;
	}

	private function getCandidate(it:BlocLinesIterator) {
		for (cmd in this.cmds) {
			// trace('cmd=$cmd');
			var nbPeek = 1;
			var bl = new BlocLines(it.peek(nbPeek));
			// trace('bl=$bl');
			var result = cmd.isValid(bl);
			// trace('result=$result');
			if (result == CommandControl.OK)
				return {
					cmd: cmd,
					bl: bl
				};

			while (result == CommandControl.OK_PARTIAL) {
				nbPeek++;
				bl = new BlocLines(it.peek(nbPeek));
				var result = cmd.isValid(bl);
				// trace('result=$result');
				if (result == CommandControl.OK)
					return {
						cmd: cmd,
						bl: bl
					};
			}
		}
		return null;
	}

	public function createSystem(lines:BlocLines):Diagram {
		final diagram = new MindMapDiagram();
		final it = lines.getBlocLinesIterator();

		while (it.hasMore()) {
			// trace('s=$s');
			// if (s == "" || s.startsWith("@start") || s.startsWith("@end"))
			// 	continue;

			final candidate = getCandidate(it);
			if (candidate == null)
				return PSystemErrorUtils.syntaxErrorAt(it.peek(1)[0]);

			final exec:CommandExecutionResult = candidate.cmd.execute(diagram, candidate.bl);
			// trace('exec=$exec');
			it.move(candidate.bl.size());

			// if (exec != CommandExecutionResult.OK)
		}
		return diagram;
	}

	public function getDiagramType():DiagramType {
		return DiagramType.MINDMAP;
	}
}
