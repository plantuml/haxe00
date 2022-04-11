package com.plantuml.sequencediagram;

class Participant {
	private final code:String;
	private var display:Display;
	private final type:ParticipantType;

	//
	//	private int initialLife = 0;
	//
	//	private Stereotype stereotype;
	//	private boolean stereotypePositionTop;
	private final hiddenPortions:Set<EntityPortion>;
	private final order:Int;
	private final styleBuilder:StyleBuilder;

	//
	//	// private Style style;
	//
	//	public StyleSignatureBasic getStyleSignature() {
	//		return type.getStyleSignature().addClickable(getUrl());
	//	}
	public function new(type:ParticipantType, code:String, display:Display, hiddenPortions:Set<EntityPortion>, order:Int, styleBuilder:StyleBuilder) {
		this.hiddenPortions = hiddenPortions;
		this.styleBuilder = styleBuilder;
		this.order = order;
		Objects.requireNonNull(code);
		this.code = code;
		if (code.length == 0) {
			throw new NotImplementedException();
		}
		//		if (Display.isNull(display) || display.size() == 0) {
		//			throw new IllegalArgumentException();
		//		}
		Objects.requireNonNull(type);
		this.type = type;
		this.display = display;
		//		// if (UseStyle.USE_STYLES()) {
		//		// this.style = getDefaultStyleDefinition().getMergedStyle(styleBuilder);
		//		// }
		//	}
	}

	public function getCode():String {
		return code;
	}

	public function getOrder() {
		return order;
	}
}
