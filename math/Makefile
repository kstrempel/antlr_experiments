ANTLR = java org.antlr.v4.Tool

compile: java.g4 python.g4
	echo "Done"

tree: compile
	javac java/*.java
	java -cp $(CLASSPATH):java org.antlr.v4.gui.TestRig Math formula formulatest.math -gui

java.g4:
	$(ANTLR) Math.g4 -Xexact-output-dir -o java -visitor -no-listener

python.g4:
	$(ANTLR) -Dlanguage=Python3 Math.g4 -Xexact-output-dir -o python -visitor -no-listener
