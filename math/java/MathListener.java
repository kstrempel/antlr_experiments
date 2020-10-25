// Generated from Math.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MathParser}.
 */
public interface MathListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MathParser#formula}.
	 * @param ctx the parse tree
	 */
	void enterFormula(MathParser.FormulaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MathParser#formula}.
	 * @param ctx the parse tree
	 */
	void exitFormula(MathParser.FormulaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code infixExpr}
	 * labeled alternative in {@link MathParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterInfixExpr(MathParser.InfixExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code infixExpr}
	 * labeled alternative in {@link MathParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitInfixExpr(MathParser.InfixExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code numberExpr}
	 * labeled alternative in {@link MathParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNumberExpr(MathParser.NumberExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code numberExpr}
	 * labeled alternative in {@link MathParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNumberExpr(MathParser.NumberExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parensExpr}
	 * labeled alternative in {@link MathParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterParensExpr(MathParser.ParensExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parensExpr}
	 * labeled alternative in {@link MathParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitParensExpr(MathParser.ParensExprContext ctx);
}