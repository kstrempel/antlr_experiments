// Generated from Indent.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link IndentParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface IndentVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link IndentParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(IndentParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by the {@code commandExpr}
	 * labeled alternative in {@link IndentParser#commands}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommandExpr(IndentParser.CommandExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code commandNewline}
	 * labeled alternative in {@link IndentParser#commands}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCommandNewline(IndentParser.CommandNewlineContext ctx);
}