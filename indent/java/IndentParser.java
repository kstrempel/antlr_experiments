// Generated from Indent.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class IndentParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NEWLINE=1, VARIABLE=2, TABS=3, INDENT=4, DEDENT=5;
	public static final int
		RULE_program = 0, RULE_commands = 1;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "commands"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\n'", null, "'-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NEWLINE", "VARIABLE", "TABS", "INDENT", "DEDENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Indent.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public IndentParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(IndentParser.EOF, 0); }
		public List<CommandsContext> commands() {
			return getRuleContexts(CommandsContext.class);
		}
		public CommandsContext commands(int i) {
			return getRuleContext(CommandsContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof IndentVisitor ) return ((IndentVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(7);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NEWLINE) | (1L << VARIABLE) | (1L << INDENT) | (1L << DEDENT))) != 0)) {
				{
				{
				setState(4);
				commands();
				}
				}
				setState(9);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(10);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CommandsContext extends ParserRuleContext {
		public CommandsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_commands; }
	 
		public CommandsContext() { }
		public void copyFrom(CommandsContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class CommandExprContext extends CommandsContext {
		public Token inden;
		public Token var;
		public TerminalNode NEWLINE() { return getToken(IndentParser.NEWLINE, 0); }
		public TerminalNode VARIABLE() { return getToken(IndentParser.VARIABLE, 0); }
		public List<TerminalNode> TABS() { return getTokens(IndentParser.TABS); }
		public TerminalNode TABS(int i) {
			return getToken(IndentParser.TABS, i);
		}
		public List<TerminalNode> INDENT() { return getTokens(IndentParser.INDENT); }
		public TerminalNode INDENT(int i) {
			return getToken(IndentParser.INDENT, i);
		}
		public List<TerminalNode> DEDENT() { return getTokens(IndentParser.DEDENT); }
		public TerminalNode DEDENT(int i) {
			return getToken(IndentParser.DEDENT, i);
		}
		public CommandExprContext(CommandsContext ctx) { copyFrom(ctx); }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof IndentVisitor ) return ((IndentVisitor<? extends T>)visitor).visitCommandExpr(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class CommandNewlineContext extends CommandsContext {
		public TerminalNode NEWLINE() { return getToken(IndentParser.NEWLINE, 0); }
		public CommandNewlineContext(CommandsContext ctx) { copyFrom(ctx); }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof IndentVisitor ) return ((IndentVisitor<? extends T>)visitor).visitCommandNewline(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CommandsContext commands() throws RecognitionException {
		CommandsContext _localctx = new CommandsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_commands);
		int _la;
		try {
			setState(27);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VARIABLE:
			case INDENT:
			case DEDENT:
				_localctx = new CommandExprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(15);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==INDENT || _la==DEDENT) {
					{
					{
					setState(12);
					((CommandExprContext)_localctx).inden = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==INDENT || _la==DEDENT) ) {
						((CommandExprContext)_localctx).inden = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					}
					setState(17);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(18);
				((CommandExprContext)_localctx).var = match(VARIABLE);
				setState(22);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==TABS) {
					{
					{
					setState(19);
					match(TABS);
					}
					}
					setState(24);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(25);
				match(NEWLINE);
				}
				break;
			case NEWLINE:
				_localctx = new CommandNewlineContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(26);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7 \4\2\t\2\4\3\t"+
		"\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2\3\2\3\2\3\3\7\3\20\n\3\f\3\16\3\23\13"+
		"\3\3\3\3\3\7\3\27\n\3\f\3\16\3\32\13\3\3\3\3\3\5\3\36\n\3\3\3\2\2\4\2"+
		"\4\2\3\3\2\6\7\2!\2\t\3\2\2\2\4\35\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\13"+
		"\3\2\2\2\t\7\3\2\2\2\t\n\3\2\2\2\n\f\3\2\2\2\13\t\3\2\2\2\f\r\7\2\2\3"+
		"\r\3\3\2\2\2\16\20\t\2\2\2\17\16\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21"+
		"\22\3\2\2\2\22\24\3\2\2\2\23\21\3\2\2\2\24\30\7\4\2\2\25\27\7\5\2\2\26"+
		"\25\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\33\3\2\2\2\32"+
		"\30\3\2\2\2\33\36\7\3\2\2\34\36\7\3\2\2\35\21\3\2\2\2\35\34\3\2\2\2\36"+
		"\5\3\2\2\2\6\t\21\30\35";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}