# List of Nodes and function specification

# List of Nodes by package

## default

* (DEV) Define New
* Accept any inputs
* Function (REMOVE?)
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

* const

## linearalgebra

* Vector

## Number

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
 
 ## boolean
 
 ## linearalgebra
 
 ## number
 
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
 "inputs": {"val": "String"},
 "outputs": {"result": "String"},
 "desc": "Converts to string."
 ```
 
 ## system
