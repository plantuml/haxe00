package com.plantuml.sequencediagram;

abstract class AbstractMessage implements EventWithDeactivate {
	private final label:Display;

	private final arrowConfiguration:ArrowConfiguration;
	// private final Set<LifeEventType> lifeEventsType = EnumSet.noneOf(LifeEventType.class);
	private var url:Url;
	private final messageNumber:String;
	// private boolean parallel = false;
	// private AbstractMessage parallelBrother;
	private final styleBuilder:StyleBuilder;

	// private List<Note> noteOnMessages = new ArrayList<>();

	public function new(styleBuilder:StyleBuilder, label:Display, arrowConfiguration:ArrowConfiguration, messageNumber:String) {
		this.styleBuilder = styleBuilder;
		this.url = null;
		this.label = label;
		this.arrowConfiguration = arrowConfiguration;
		this.messageNumber = messageNumber;
	}
}
