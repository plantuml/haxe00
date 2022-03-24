package com.plantuml;

import com.plantuml.command.BlocLines;
import com.plantuml.core.Diagram;
import com.plantuml.core.DiagramType;
import com.plantuml.mindmap.MindMapDiagramFactory;

using com.plantuml.ArrayExtensions;
using com.plantuml.utils.StartUtils;

class PSystemBuilder {
	private final factories:Array<PSystemFactory> = [];

	public function new() {
		factories.push(new MindMapDiagramFactory());
	}

	public function createPSystem(lines:BlocLines):Diagram {
		lines = lines.findStartSomething();
		if (lines == null)
			return null;

		final type = DiagramType.getTypeFromArobaseStart(lines.getFirst());
		lines = lines.removeFirstAndLast();
		for (f in factories.filter(x -> x.getDiagramType() == type)) {
			final result = f.createSystem(lines);
			if (result != null)
				return result;
		}

		return null;
	}
}
