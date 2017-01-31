# Official node specification

This document is the official node specification sheet.
From a users point of view this is a documentation of all nodes that will be availible on any graph programming kernel (that meets the official specificaton).

## Short note for kernel/node developers

Each graph programming kernel must implement all nodes specified in here.
It also should not implement any node that is not specified (in the stdlib).

You are free to write any nodes in the extlib (for publishing) or the privatelib (for private use).
However these nodes are specific to a language and not be availible across all languages.

If you write optimized algorithms in a language specific extlib that can be expressed as graph programming graphs, please provide the graph, so it can run unoptimized on other languages.

# List of nodes by package

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

## debug

* View

## linearalgebra

* Vector
* Vector Trigger

## number

* Arg Const
* Arg Trigger
* Const
* Div
* Equal
* Greater
* Increase Trigger
* Less
* Mult
* Subtract
* Sum
* Trigger

## string

* Arg Const
* Arg Trigger
* Concat
* Const
* Ends With
* Equal
* Index Of
* Split
* Starts With
* Trigger
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
 
## debug

### stdlib.debug.view
 ```json
 "name": "View",
 "inputs": {"val": "Object"},
 "outputs": {"result": "Object"},
 "args": {"width": 0, "height": 0},
 "desc": "Views and passes the object."
 ```

## linearalgebra
 
### stdlib.linearalgebra.vector
 ```json
 "name": "Vector",
 "outputs": {"result": "Vector"},
 "args": {"value": [1, 0, 0]}
 "desc": "A simple vector."
 ```
 
### stdlib.linearalgebra.vectortrigger
 ```json
 "name": "Vector Trigger",
 "outputs": {"result": "Vector"},
 "args": {"value": [1, 0, 0], "time": 1.0}
 "desc": "A simple vector."
 ```

## number
 
### stdlib.number.argconst
 ```json
 "name": "Arg Const",
 "outputs": {"result": "Number"},
 "args": {"arg": "a"},
 "desc": "Outputs a variable from the state of a graph."
 ```

### stdlib.number.argtrigger
 ```json
 "name": "Arg Trigger",
 "outputs": {"result": "Number"},
 "args": {"arg": "a"},
 "desc": "Triggers a variable from the state of a graph."
 ```

### stdlib.number.const
 ```json
 "name": "Const",
 "outputs": {"result": "Number"},
 "args": {"value": 0},
 "desc": "A constant number."
 ```
 
### stdlib.number.div
 ```json
 "name": "Div",
 "inputs": {"a": "Number", "b": "Number"},
 "outputs": {"result": "Number"},
 "desc": "Divides a by b."
 ```

### stdlib.number.equal
 ```json
 "name": "Equal",
 "inputs": {"a": "Number", "b": "Number"},
 "outputs": {"result": "Boolean"},
 "desc": "Checks if a and b are equal."
 ```

### stdlib.number.greater
 ```json
 "name": "Greater",
 "inputs": {"a": "Number", "b": "Number"},
 "outputs": {"result": "Boolean"},
 "desc": "Checks if a > b."
 ```

### stdlib.number.increasetrigger
 ```json
 "name": "Increase Trigger",
 "outputs": {"result": "Number"},
 "args": {"value": 0, "time": 1.0},
 "desc": "Triggers value and increases it every [time]s."
 ```
 
### stdlib.number.less
 ```json
 "name":"Less",
 "inputs": {"a": "Number", "b": "Number"},
 "outputs": {"result": "Boolean"},
 "desc": "Checks if a < b."
 ```

### stdlib.number.mult
 ```json
 "name": "Mult",
 "inputs": {"a": "Number", "b": "Number"},
 "outputs": {"result": "Number"},
 "desc": "a * b."
 ```
 
### stdlib.number.subtract
 ```json
 "name": "Subtract",
 "inputs": {"a": "Number", "b": "Number"},
 "outputs": {"result": "Number"},
 "desc": "a - b."
 ```
 
### stdlib.number.sum
 ```json
 "name": "Sum",
 "inputs": {"a": "Number", "b": "Number"},
 "outputs": {"result": "Number"},
 "desc": "a + b."
 ```
 
### stdlib.number.trigger
 ```json
 "name": "Trigger",
 "outputs": {"result": "Number"},
 "args": {"value": 0, "time": 1.0},
 "desc": "Triggers value every [time]s."
 ```
 
## string
 
### stdlib.string.argconst
 ```json
 "name": "Arg Const",
 "outputs": {"result": "String"},
 "args": {"arg": "a"},
 "desc": "Returns the global variable in [arg]."
 ```
 
### stdlib.string.argtrigger
 ```json
 "name": "Arg Trigger",
 "outputs": {"result": "String"},
 "args": {"arg": "a", "time": 1.0},
 "desc": "Returns the global variable in [arg] every [time]s."
 ```
 
### stdlib.string.concat
 ```json
 "name": "Concat",
 "inputs": {"left": "String", "right": "String"},
 "outputs": {"result": "String"},
 "desc": "Concat left and right."
 ```
 
### stdlib.string.const
 ```json
 "name": "Const",
 "outputs": {"result": "String"},
 "args": {"value": "Hello World!"},
 "desc": "Returns the arg on the output."
 ```
 
### stdlib.string.endswith
 ```json
 "name": "Ends With",
 "inputs": {"val": "String", "needle": "String"}
 "outputs": {"result": "Boolean"},
 "desc": "Does a string [val] end with [needle]?"
 ```
 
### stdlib.string.equal
 ```json
 "name": "Equal",
 "inputs": {"a": "String", "b": "String"}
 "outputs": {"result": "Boolean"},
 "desc": "Returns true if a and b are equal"
 ```
 
### stdlib.string.indexof
 ```json
 "name": "Index Of",
 "inputs": {"val": "String", "needle": "String"}
 "outputs": {"result": "Number"},
 "desc": "Where does a string [val] contain [needle]? (-1 if not found)"
 ```
 
### stdlib.string.split
 ```json
 "name": "Split",
 "inputs": {"val": "String"}
 "outputs": {"result": "[String]"},
 "args": {"delim":";"},
 "desc": "Splits [val] with [delim]."
 ```
 
### stdlib.string.startswith
 ```json
 "name": "Starts With",
 "inputs": {"val": "String", "needle": "String"}
 "outputs": {"result": "Boolean"},
 "desc": "Does a string [val] start with [needle]?"
 ```
 
### stdlib.string.trigger
 ```json
 "name": "Trigger",
 "outputs": {"result": "String"},
 "args": {"value":"Hello World!", "time": 1.0}
 "desc": "Outputs [value] every [time]s."
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
