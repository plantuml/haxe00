package com.plantuml.sequencediagram;

import com.plantuml.sequencediagram.command.*;
import com.plantuml.error.*;
import com.plantuml.core.*;
import com.plantuml.command.*;

using hx.strings.Strings;

class SequenceDiagramFactory extends PSystemCommandFactory<SequenceDiagram> {
	public function new() {
		super(createCommands());
	}

	private function createCommands():Array<Command<SequenceDiagram>> {
		var cmds:Array<Command<SequenceDiagram>> = [];

		// CommonCommands.addCommonCommands1(cmds);
		// cmds.add(new CommandHideUnlinked());

		// cmds.add(new CommandActivate());
		// cmds.add(new CommandDeactivateShort());

		// cmds.add(new CommandParticipantA());
		// cmds.add(new CommandParticipantA2());
		// cmds.add(new CommandParticipantA3());
		// cmds.add(new CommandParticipantA4());
		// cmds.add(new CommandParticipantMultilines());
		cmds.push(new CommandArrow());
		// // addCommand(new CommandArrowCrossX());
		// cmds.add(new CommandExoArrowLeft());
		// cmds.add(new CommandExoArrowRight());

		// final FactorySequenceNoteCommand factorySequenceNoteCommand = new FactorySequenceNoteCommand();
		// cmds.add(factorySequenceNoteCommand.createSingleLine());

		// final FactorySequenceNoteOverSeveralCommand factorySequenceNoteOverSeveralCommand = new FactorySequenceNoteOverSeveralCommand();
		// cmds.add(factorySequenceNoteOverSeveralCommand.createSingleLine());
		// final FactorySequenceNoteAcrossCommand factorySequenceNoteAcrossCommand = new FactorySequenceNoteAcrossCommand();
		// cmds.add(factorySequenceNoteAcrossCommand.createSingleLine());

		// cmds.add(new CommandBoxStart());
		// cmds.add(new CommandBoxEnd());
		// cmds.add(new CommandGrouping());

		// cmds.add(new CommandActivate2());
		// cmds.add(new CommandReturn());

		// final FactorySequenceNoteOnArrowCommand factorySequenceNoteOnArrowCommand = new FactorySequenceNoteOnArrowCommand();
		// cmds.add(factorySequenceNoteOnArrowCommand.createSingleLine());

		// cmds.add(factorySequenceNoteCommand.createMultiLine(false));
		// cmds.add(factorySequenceNoteOverSeveralCommand.createMultiLine(false));
		// cmds.add(factorySequenceNoteOnArrowCommand.createMultiLine(false));
		// cmds.add(factorySequenceNoteAcrossCommand.createMultiLine(false));

		// cmds.add(new CommandNewpage());
		// cmds.add(new CommandIgnoreNewpage());
		// cmds.add(new CommandAutoNewpage());
		// cmds.add(new CommandDivider());
		// cmds.add(new CommandHSpace());
		// cmds.add(new CommandReferenceOverSeveral());
		// cmds.add(new CommandReferenceMultilinesOverSeveral());
		// cmds.add(new CommandAutonumber());
		// cmds.add(new CommandAutonumberStop());
		// cmds.add(new CommandAutonumberResume());
		// cmds.add(new CommandAutonumberIncrement());
		// cmds.add(new CommandAutoactivate());
		// cmds.add(new CommandFootbox());
		// cmds.add(new CommandDelay());
		// cmds.add(new CommandFootboxOld());
		// cmds.add(new CommandUrl());
		// cmds.add(new CommandLinkAnchor());

		return cmds;
	}

	function createEmpty() {
		return new SequenceDiagram();
	}

	public function getDiagramType():DiagramType {
		return DiagramType.UML;
	}
}
