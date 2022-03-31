package com.plantuml;

interface PSystemFactory {
	public function createSystem(lines:BlocLines):Diagram;
	public function getDiagramType():DiagramType;
}
