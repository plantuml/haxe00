package com.plantuml.cucadiagram;

@:enum
abstract EntityPortion(String) {
	final FIELD;
	final METHOD;
	final MEMBER;
	final CIRCLED_CHARACTER;
	final STEREOTYPE;

	public function asSet():Set<EntityPortion> {
		// if (this == MEMBER) {
		// 	return EnumSet.<EntityPortion> of(FIELD, METHOD);
		// }
		// return EnumSet.<EntityPortion> of(this);
		throw new NotImplementedException();
	}
}
