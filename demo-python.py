#!/usr/bin/python
import libplantuml

if __name__ == "__main__":
    plantuml = libplantuml.Plantuml()
    plantuml.addLineSingle("* World")
    plantuml.addLineSingle("** America")
    plantuml.addLineSingle("** Europ")
    svg = plantuml.getSvg()
    print(svg)
