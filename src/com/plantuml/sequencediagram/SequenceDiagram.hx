package com.plantuml.sequencediagram;

class SequenceDiagram extends Diagram {
	private final skinParam = new SkinParam();

	//	private boolean hideUnlinkedData;
	//
	//	public final boolean isHideUnlinkedData() {
	//		return hideUnlinkedData;
	//	}
	//
	//	public final void setHideUnlinkedData(boolean hideUnlinkedData) {
	//		this.hideUnlinkedData = hideUnlinkedData;
	//	}
	//
	private final events:Array<Event> = [];
	//
	//	private final Map<Participant, ParticipantEnglober> participantEnglobers2 = new HashMap<Participant, ParticipantEnglober>();
	private final participantEnglobers2:Map<Participant, ParticipantEnglober> = [];
	private var participantEnglober:ParticipantEnglober;
	private final hiddenPortions:Set<EntityPortion>;
	private final participantsList:Array<Participant> = [];

	public function new() {
		this.hiddenPortions = null;
	}

	public function getOrCreateParticipant(code:String, display:Display):Participant {
		var result:Participant = participantsget(code);
		if (result == null) {
			result = new Participant(ParticipantType.PARTICIPANT, code, display, hiddenPortions, 0, getSkinParam().getCurrentStyleBuilder());
			addWithOrder(result);
			participantEnglobers2[result] = participantEnglober;
		}
		return result;

		throw new haxe.exceptions.NotImplementedException();
	}

	private function participantsget(code:String):Participant {
		for (p in participantsList)
			if (p.getCode().equals(code))
				return p;

		return null;
	}

	private function addWithOrder(result:Participant) {
		for (i in 0...participantsList.length)
			if (result.getOrder() < participantsList[i].getOrder()) {
				participantsList.insert(i, result);
				return;
			}

		participantsList.push(result);
	}

	public function getSkinParam():SkinParam {
		return skinParam;
	}

	public function activate(p:Participant, lifeEventType:LifeEventType, backcolor:HColor) {
		throw new haxe.exceptions.NotImplementedException();
	}

	private final autoNumber = new AutoNumber();

	public function getNextMessageNumber() {
		return autoNumber.getNextMessageNumber();
	}

	public function manageVariable(labels:Display):Display {
		return labels;
	}

	public function addMessage(m:AbstractMessage) {
		//		if (m.isParallel())
		//			m.setParallelBrother(getLastAbstractMessage());
		//
		//		lastEventWithDeactivate = m;
		//		lastDelay = null;
		events.push(m);
		//		if (pendingCreate != null) {
		//			if (m.compatibleForCreate(pendingCreate.getParticipant()) == false)
		//				return "After create command, you have to send a message to \"" + pendingCreate.getParticipant() + "\"";
		//
		//			m.addLifeEvent(pendingCreate);
		//			pendingCreate = null;
		//		}
		return null;
	}

	public function exportDiagramNow(ug:UGraphic) {
		throw new NotImplementedException();
	}
}
