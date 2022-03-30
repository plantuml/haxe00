package com.plantuml;

import com.plantuml.command.*;
import com.plantuml.core.*;
import com.plantuml.eggs.*;
import com.plantuml.error.*;
import com.plantuml.mindmap.*;
import com.plantuml.sequencediagram.*;

using com.plantuml.ArrayExtensions;
using com.plantuml.utils.StartUtils;

class PSystemBuilder {
	private final factories:Array<PSystemFactory> = [];

	public function new() {
		factories.push(new CharSizeDiagramFactory());
		factories.push(new SequenceDiagramFactory());
		factories.push(new MindMapDiagramFactory());
	}

	public function createPSystem(lines:BlocLines):Diagram {
		lines = lines.findStartSomething();
		if (lines == null)
			return new DiagramNothingFound([]);

		final type = DiagramType.getTypeFromArobaseStart(lines.getFirst());

		if (type == UNKNOWN)
			return new DiagramNothingFound(lines.getLines());

		lines = lines.removeFirstAndLast();
		for (f in factories.filter(x -> x.getDiagramType() == type)) {
			try {
				// trace('f=$f');
				final result = f.createSystem(lines);
				if (result != null)
					return result;
			} catch (e) {
				trace("Error in some factory");
				trace(e.message);
				return PSystemErrorUtils.crashErrorAt(e);
			}
		}
		trace("No factory found!");
		return new DiagramNothingFound(lines.getLines());
	}
}
