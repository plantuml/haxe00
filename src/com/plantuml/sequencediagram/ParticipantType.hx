package com.plantuml.sequencediagram;

@:enum
abstract ParticipantType(String) {
	final PARTICIPANT; // (ColorParam.participantBackground), //
	final ACTOR; // (ColorParam.actorBackground), //
	final BOUNDARY; // ColorParam.boundaryBackground), //
	final CONTROL; // (ColorParam.controlBackground), //
	final ENTITY; // (ColorParam.entityBackground), //
	final QUEUE; // (ColorParam.queueBackground), //
	final DATABASE; // (ColorParam.databaseBackground), //
	final COLLECTIONS; // (ColorParam.collectionsBackground);
}
