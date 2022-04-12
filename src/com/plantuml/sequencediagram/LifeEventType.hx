package com.plantuml.sequencediagram;

@:enum
abstract LifeEventType(String) {
	final ACTIVATE;
	final DEACTIVATE;
	final DESTROY;
	final CREATE;
}
