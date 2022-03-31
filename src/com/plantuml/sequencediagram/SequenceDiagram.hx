package com.plantuml.sequencediagram;

class SequenceDiagram {
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
	private final participantsList:Array<Participant> = [];

	//
	//	private final List<Event> events = new ArrayList<>();
	//
	//	private final Map<Participant, ParticipantEnglober> participantEnglobers2 = new HashMap<Participant, ParticipantEnglober>();

	public function new() {}

	public function getOrCreateParticipant(code:String, display:Display):Participant {
		//		Participant result = participantsget(code);
		//		if (result == null) {
		//			result = new Participant(ParticipantType.PARTICIPANT, code, display, hiddenPortions, 0,
		//					getSkinParam().getCurrentStyleBuilder());
		//			addWithOrder(result);
		//			participantEnglobers2.put(result, participantEnglober);
		//		}
		//		return result;

		throw new haxe.exceptions.NotImplementedException();
	}

	private function participantsget(code:String):Participant {
		for (p in participantsList)
			if (p.getCode().equals(code))
				return p;

		return null;
	}
}
