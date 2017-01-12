# Official node specification

This document is the official node specification sheet.
From a users point of view this is a documentation of all nodes that will be availible on any graph programming kernel (that meets the official specificaton).

## Short note for kernel/node developers

Each graph programming kernel must implement all nodes specified in here.
It also should not implement any node that is not specified (in the stdlib).

You are free to write any nodes in the extlib (for publishing) or the privatelib (for private use).
However these nodes are specific to a language and not be availible across all languages.

If you write optimized algorithms in a language specific extlib that can be expressed as graph programming graphs, please provide the graph, so it can run unoptimized on other languages.

# List of Nodes by package

## default

* (DEV) Define New
* Accept any inputs
* Function (REMOVE? Its unsafe and you could simply write a real node)
* Pass
* Splitflow 2
* Splitflow 5

## structures

* For
* If
* Sync
* While greater
* While less
* Limit

## boolean

* Const

## linearalgebra

* Vector

## number

* Const
* Mult

## string

 * String Concat
 * String Const
 * toString
 
## system
 
 * Print
 
 
# Node (specific) Specification by Package
 
## default

## structures
 
### stdlib.structures.if
 ```json
 "name": "If",
 "inputs": {"val": "Object", "condition": "Boolean"},
 "outputs": {"true": "Object", "false": "Object"},
 "desc": "Pass val based on condition."
 ```
 
## boolean
 
### stdlib.boolean.const
 ```json
 "name": "Const",
 "outputs": {"result": "Boolean"},
 "args": {"value": true},
 "desc": "Return a const boolean."
 ```
 
## linearalgebra
 
### stdlib.linearalgebra.vector
 ```json
 "name": "Vector",
 "outputs": {"result": "Vector"},
 "args": {"value": [1, 0, 0]}
 "desc": "A simple vector."
 ```
 
## number
 
### stdlib.number.const
 ```json
 "name": "Const",
 "outputs": {"result": "Number"},
 "args": {"value": 0},
 "desc": "A constant number."
 ```
 
### stdlib.number.mult
 ```json
 "name": "Mult",
 "inputs": {"a": "Number", "b": "Number"},
 "outputs": {"result": "Number"},
 "desc": "a * b."
 ```
 
## string
 
### stdlib.string.const
 ```json
 "name": "String Const",
 "outputs": {"result": "String"},
 "args": {"value": "Hello World!"},
 "desc": "Returns the arg on the output."
 ```
 
### stdlib.string.concat
 ```json
 "name": "String Concat",
 "inputs": {"left": "String", "right": "String"},
 "outputs": {"result": "String"},
 "desc": "Concat left and right."
 ```
 
### stdlib.string.tostr
 ```json
 "name": "toString",
 "inputs": {"val": "Object"},
 "outputs": {"result": "String"},
 "desc": "Converts to string."
 ```
 
## system
 
### stdlib.system.print
 ```json
 "name": "Print",
 "inputs": {"val": "Object"},
 "desc": "Prints on the screen."
 ```
