package com.plantuml.command;

import com.plantuml.error.*;
import com.plantuml.core.*;
import com.plantuml.command.*;

abstract class PSystemCommandFactory<D> implements PSystemFactory {
	var cmds:Array<Command<D>>;

	public function new(cmds) {
		this.cmds = cmds;
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

	abstract function createEmpty():D;

	public function createSystem(lines:BlocLines):Diagram {
		final diagram = createEmpty();
		final it = lines.getBlocLinesIterator();

		while (it.hasMore()) {
			// trace('s=$s');
			// if (s == "" || s.startsWith("@start") || s.startsWith("@end"))
			// 	continue;

			final candidate = getCandidate(it);
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
