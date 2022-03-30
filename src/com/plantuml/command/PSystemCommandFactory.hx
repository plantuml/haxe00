package com.plantuml.command;

import com.plantuml.error.PSystemErrorUtils;
import com.plantuml.core.DiagramType;
import com.plantuml.core.Diagram;
import com.plantuml.command.BlocLines;

abstract class PSystemCommandFactory<D> implements PSystemFactory {
	var cmds2:Array<Command<D>>;

	public function new(cmds2) {
		this.cmds2 = cmds2;
	}

	private function getCandidate2(it:BlocLinesIterator) {
		for (cmd in this.cmds2) {
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
				final tmp = it.peek(nbPeek);
				if (tmp == null)
					return null;
				bl = new BlocLines(tmp);
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

	abstract function createEmpty2():D;

	public function createSystem2(lines:BlocLines):Diagram {
		final diagram = createEmpty2();
		final it = lines.getBlocLinesIterator();

		while (it.hasMore()) {
			// trace('s=$s');
			// if (s == "" || s.startsWith("@start") || s.startsWith("@end"))
			// 	continue;

			final candidate = getCandidate2(it);
			if (candidate == null)
				return PSystemErrorUtils.syntaxErrorAt(lines.slice(0, it.currentPosition() + 1));

			final exec:CommandExecutionResult = candidate.cmd.execute(diagram, candidate.bl);
			// trace('exec=$exec');
			it.move(candidate.bl.size());

			// if (exec != CommandExecutionResult.OK)
		}
		return cast(diagram, Diagram);
	}
}
