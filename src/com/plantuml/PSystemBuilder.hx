package com.plantuml;

import com.plantuml.core.DiagramType.DiagramTypeUtils;
import com.plantuml.command.BlocLines;

using com.plantuml.utils.StartUtils;
using com.plantuml.ArrayExtensions;

import com.plantuml.mindmap.MindMapDiagramFactory;
import com.plantuml.core.Diagram;

class PSystemBuilder {
	private final factories:Array<PSystemFactory> = [];

	public function new() {
		factories.push(new MindMapDiagramFactory());
	}

	public function createPSystem(lines:BlocLines):Diagram {
		lines = lines.findStartSomething();
		if (lines == null)
			return null;

		final type = DiagramTypeUtils.getTypeFromArobaseStart(lines.getFirst());
		lines = lines.removeFirstAndLast();
		for (f in factories.filter(x -> x.getDiagramType() == type)) {
			final result = f.createSystem(lines);
			if (result != null)
				return result;
		}

		return null;
	}
}
