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

	public function createPSystem(data:Array<String>):Diagram {
		if (data[0].isArobaseStartDiagram() == false)
			throw new haxe.exceptions.NotImplementedException();
		if (data.last().isArobaseEndDiagram() == false)
			throw new haxe.exceptions.NotImplementedException();

		final type = DiagramTypeUtils.getTypeFromArobaseStart(data[0]);
		data = data.removeFirstAndLast();
		final lines = new BlocLines(data);
		for (f in factories.filter(x -> x.getDiagramType() == type)) {
			final result = f.createSystem(lines);
			if (result != null)
				return result;
		}

		return null;
	}
}
