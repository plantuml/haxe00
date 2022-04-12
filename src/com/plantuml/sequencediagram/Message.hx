package com.plantuml.sequencediagram;

class Message extends AbstractMessage {
	private final p1:Participant;
	private final p2:Participant;

	public function new(styleBuilder:StyleBuilder, p1:Participant, p2:Participant, label:Display, arrowConfiguration:ArrowConfiguration,
			messageNumber:String) {
		super(styleBuilder, label, arrowConfiguration, messageNumber);
		this.p1 = p1;
		this.p2 = p2;
	}

	public function dealWith(someone:Participant):Bool {
		return someone == p1 || someone == p2;
	}
}
