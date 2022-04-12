package com.plantuml.sequencediagram;

interface Event {
	public function dealWith(someone:Participant):Bool;
	//
	//	Url getUrl();
	//
	//	boolean hasUrl();
	//
	//	boolean isParallel();
}
