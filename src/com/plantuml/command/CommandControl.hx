package com.plantuml.command;

@:enum
abstract CommandControl(String) {
	final OK;
	final NOT_OK;
	final OK_PARTIAL;
}
