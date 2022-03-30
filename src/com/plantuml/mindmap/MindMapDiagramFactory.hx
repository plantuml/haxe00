package com.plantuml.mindmap;

import com.plantuml.error.*;
import com.plantuml.core.*;
import com.plantuml.command.*;

using hx.strings.Strings;

class MindMapDiagramFactory extends PSystemCommandFactory<MindMapDiagram> {
	public function new() {
		super(createCommands());
	}

	private function createCommands():Array<Command<MindMapDiagram>> {
		var cmds:Array<Command<MindMapDiagram>> = [];
		// CommonCommands.addCommonCommands1(cmds);

		cmds.push(new CommandMindMapOrgmode());
		cmds.push(new CommandMindMapOrgmodeMultiline());
		cmds.push(new CommandMindMapRoot());
		cmds.push(new CommandMindMapPlus());
		cmds.push(new CommandMindMapDirection());

		return cmds;
	}

	function createEmpty() {
		return new MindMapDiagram();
	}

	public function getDiagramType():DiagramType {
		return DiagramType.MINDMAP;
	}
}
