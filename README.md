###### By Fiodel

# ChemiCompilerCompiler

#### A Program to write programs for the ChemiCompiler in Goonstation SS13

##### See the guide to the ChemiCompiler in the wiki here: https://wiki.ss13.co/ChemiCompiler

The ChemiCompiler inside of Goonstation streamlines the chemical making process, whether
you're trying to make beaker bombs, or poisons. However, there are two barriers to use: understanding the language of the ChemiCompiler,
and writing the programs themselves.

Here's where the ChemiCompilerCompiler steps in. Given a series of commands, it can convert them into ChemFuck,
which can be used in the ChemiCompiler.

The three commands are as listed: 

`MOVE 1 2 25` will move 25 units of reagent from beaker 1 (source) to beaker 2 (target)

`TEMP 9 400` will heat/cool beaker 9 (source) to 400 degrees K

`ISOLATE 4 3 10 1` will isolate 10 units of reagent number 1 from beaker 4 (source) to beaker 3 (target)

##### To use

Go into the Standard folder, and run Driver.py. Input the name of your text file containing the commands, and the program will
print out the resulting ChemFuck.

