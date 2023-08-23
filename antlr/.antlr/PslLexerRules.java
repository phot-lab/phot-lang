// Generated from d:\科研项目\PhotLab\phot-lang\antlr\PslLexerRules.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PslLexerRules extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		AS=1, LET=2, USE=3, FUNC=4, TYPE=5, ENUM=6, WITH=7, RETURN=8, INNER=9, 
		SYNC=10, SCOPED=11, STATIC=12, ATOMIC=13, NULL=14, TRUE=15, FALSE=16, 
		ANY_TYPE=17, NUMBER_TYPE=18, STRING_TYPE=19, BOOLEAN_TYPE=20, FUNCTOR_TYPE=21, 
		BLOCK_TYPE=22, INTEGER_TYPE=23, REAL_TYPE=24, COMPLEX_TYPE=25, ARRAY_TYPE=26, 
		MATRIX_TYPE=27, LIST_TYPE=28, DICT_TYPE=29, SKIP_=30, LINE_END=31, MULTI_STR=32, 
		IDENTIFIER=33, UNIT=34, STRING=35, FSTRING=36, INTEGER=37, REAL=38;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"AS", "LET", "USE", "FUNC", "TYPE", "ENUM", "WITH", "RETURN", "INNER", 
			"SYNC", "SCOPED", "STATIC", "ATOMIC", "NULL", "TRUE", "FALSE", "ANY_TYPE", 
			"NUMBER_TYPE", "STRING_TYPE", "BOOLEAN_TYPE", "FUNCTOR_TYPE", "BLOCK_TYPE", 
			"INTEGER_TYPE", "REAL_TYPE", "COMPLEX_TYPE", "ARRAY_TYPE", "MATRIX_TYPE", 
			"LIST_TYPE", "DICT_TYPE", "SKIP_", "LINE_END", "BLANK", "LIN_CMT", "BLK_CMT", 
			"LINE_MID", "MULTI_STR", "IDENTIFIER", "UNIT", "STRING", "FSTRING", "INTEGER", 
			"REAL", "DECIMAL", "OCTAL", "HEXADECIMAL", "BINARY", "FLOAT", "EXPONENT_FLOAT", 
			"EXPONENT_DECIMAL", "EXPONENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'as'", "'let'", "'use'", "'func'", "'type'", "'enum'", "'with'", 
			"'return'", "'inner'", "'sync'", "'scoped'", "'static'", "'atomic'", 
			"'null'", "'true'", "'false'", "'any'", "'number'", "'string'", "'bool'", 
			"'functor'", "'block'", "'int'", "'real'", "'complex'", "'array'", "'matrix'", 
			"'list'", "'dict'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "AS", "LET", "USE", "FUNC", "TYPE", "ENUM", "WITH", "RETURN", "INNER", 
			"SYNC", "SCOPED", "STATIC", "ATOMIC", "NULL", "TRUE", "FALSE", "ANY_TYPE", 
			"NUMBER_TYPE", "STRING_TYPE", "BOOLEAN_TYPE", "FUNCTOR_TYPE", "BLOCK_TYPE", 
			"INTEGER_TYPE", "REAL_TYPE", "COMPLEX_TYPE", "ARRAY_TYPE", "MATRIX_TYPE", 
			"LIST_TYPE", "DICT_TYPE", "SKIP_", "LINE_END", "MULTI_STR", "IDENTIFIER", 
			"UNIT", "STRING", "FSTRING", "INTEGER", "REAL"
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


	public PslLexerRules(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "PslLexerRules.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2(\u01f1\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\3\2"+
		"\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3"+
		"\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30"+
		"\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32"+
		"\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34"+
		"\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37"+
		"\5\37\u010f\n\37\3\37\3\37\3 \6 \u0114\n \r \16 \u0115\3!\6!\u0119\n!"+
		"\r!\16!\u011a\3\"\3\"\3\"\3\"\7\"\u0121\n\"\f\"\16\"\u0124\13\"\3\"\3"+
		"\"\3\"\3\"\7\"\u012a\n\"\f\"\16\"\u012d\13\"\5\"\u012f\n\"\3#\3#\3#\3"+
		"#\7#\u0135\n#\f#\16#\u0138\13#\3#\3#\3#\3#\3#\3#\3#\7#\u0141\n#\f#\16"+
		"#\u0144\13#\3#\3#\3#\5#\u0149\n#\3$\3$\5$\u014d\n$\3$\3$\3%\3%\3%\3%\3"+
		"%\7%\u0156\n%\f%\16%\u0159\13%\3%\3%\3%\3%\3%\3%\3%\3%\7%\u0163\n%\f%"+
		"\16%\u0166\13%\3%\3%\3%\5%\u016b\n%\3&\3&\7&\u016f\n&\f&\16&\u0172\13"+
		"&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u017a\n\'\f\'\16\'\u017d\13\'\3\'\3\'\3"+
		"(\3(\3(\3(\3(\3(\7(\u0187\n(\f(\16(\u018a\13(\3(\3(\3(\3(\3(\3(\3(\7("+
		"\u0193\n(\f(\16(\u0196\13(\3(\5(\u0199\n(\3)\3)\3)\3*\3*\3*\3*\3*\5*\u01a3"+
		"\n*\3+\3+\5+\u01a7\n+\3,\5,\u01aa\n,\3,\3,\7,\u01ae\n,\f,\16,\u01b1\13"+
		",\3,\5,\u01b4\n,\3-\5-\u01b7\n-\3-\3-\6-\u01bb\n-\r-\16-\u01bc\3.\5.\u01c0"+
		"\n.\3.\3.\3.\3.\6.\u01c6\n.\r.\16.\u01c7\3/\5/\u01cb\n/\3/\3/\3/\3/\6"+
		"/\u01d1\n/\r/\16/\u01d2\3\60\5\60\u01d6\n\60\3\60\6\60\u01d9\n\60\r\60"+
		"\16\60\u01da\3\60\3\60\6\60\u01df\n\60\r\60\16\60\u01e0\3\61\3\61\3\61"+
		"\3\62\3\62\3\62\3\63\3\63\5\63\u01eb\n\63\3\63\6\63\u01ee\n\63\r\63\16"+
		"\63\u01ef\t\u0136\u0142\u0157\u0164\u017b\u0188\u0194\2\64\3\3\5\4\7\5"+
		"\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23"+
		"%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\2C\2E\2"+
		"G\2I\"K#M$O%Q&S\'U(W\2Y\2[\2]\2_\2a\2c\2e\2\3\2\16\4\2\f\f\17\17\5\2\13"+
		"\13\16\16\"\"\4\2\f\f\16\17\5\2C\\aac|\6\2\62;C\\aac|\4\2--//\3\2\63;"+
		"\3\2\62;\3\2\629\5\2\62;CHch\3\2\62\63\4\2GGgg\2\u0211\2\3\3\2\2\2\2\5"+
		"\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2"+
		"\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33"+
		"\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2"+
		"\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2"+
		"\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2"+
		"\2?\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S"+
		"\3\2\2\2\2U\3\2\2\2\3g\3\2\2\2\5j\3\2\2\2\7n\3\2\2\2\tr\3\2\2\2\13w\3"+
		"\2\2\2\r|\3\2\2\2\17\u0081\3\2\2\2\21\u0086\3\2\2\2\23\u008d\3\2\2\2\25"+
		"\u0093\3\2\2\2\27\u0098\3\2\2\2\31\u009f\3\2\2\2\33\u00a6\3\2\2\2\35\u00ad"+
		"\3\2\2\2\37\u00b2\3\2\2\2!\u00b7\3\2\2\2#\u00bd\3\2\2\2%\u00c1\3\2\2\2"+
		"\'\u00c8\3\2\2\2)\u00cf\3\2\2\2+\u00d4\3\2\2\2-\u00dc\3\2\2\2/\u00e2\3"+
		"\2\2\2\61\u00e6\3\2\2\2\63\u00eb\3\2\2\2\65\u00f3\3\2\2\2\67\u00f9\3\2"+
		"\2\29\u0100\3\2\2\2;\u0105\3\2\2\2=\u010e\3\2\2\2?\u0113\3\2\2\2A\u0118"+
		"\3\2\2\2C\u012e\3\2\2\2E\u0148\3\2\2\2G\u014a\3\2\2\2I\u016a\3\2\2\2K"+
		"\u016c\3\2\2\2M\u0173\3\2\2\2O\u0198\3\2\2\2Q\u019a\3\2\2\2S\u01a2\3\2"+
		"\2\2U\u01a6\3\2\2\2W\u01a9\3\2\2\2Y\u01b6\3\2\2\2[\u01bf\3\2\2\2]\u01ca"+
		"\3\2\2\2_\u01d5\3\2\2\2a\u01e2\3\2\2\2c\u01e5\3\2\2\2e\u01e8\3\2\2\2g"+
		"h\7c\2\2hi\7u\2\2i\4\3\2\2\2jk\7n\2\2kl\7g\2\2lm\7v\2\2m\6\3\2\2\2no\7"+
		"w\2\2op\7u\2\2pq\7g\2\2q\b\3\2\2\2rs\7h\2\2st\7w\2\2tu\7p\2\2uv\7e\2\2"+
		"v\n\3\2\2\2wx\7v\2\2xy\7{\2\2yz\7r\2\2z{\7g\2\2{\f\3\2\2\2|}\7g\2\2}~"+
		"\7p\2\2~\177\7w\2\2\177\u0080\7o\2\2\u0080\16\3\2\2\2\u0081\u0082\7y\2"+
		"\2\u0082\u0083\7k\2\2\u0083\u0084\7v\2\2\u0084\u0085\7j\2\2\u0085\20\3"+
		"\2\2\2\u0086\u0087\7t\2\2\u0087\u0088\7g\2\2\u0088\u0089\7v\2\2\u0089"+
		"\u008a\7w\2\2\u008a\u008b\7t\2\2\u008b\u008c\7p\2\2\u008c\22\3\2\2\2\u008d"+
		"\u008e\7k\2\2\u008e\u008f\7p\2\2\u008f\u0090\7p\2\2\u0090\u0091\7g\2\2"+
		"\u0091\u0092\7t\2\2\u0092\24\3\2\2\2\u0093\u0094\7u\2\2\u0094\u0095\7"+
		"{\2\2\u0095\u0096\7p\2\2\u0096\u0097\7e\2\2\u0097\26\3\2\2\2\u0098\u0099"+
		"\7u\2\2\u0099\u009a\7e\2\2\u009a\u009b\7q\2\2\u009b\u009c\7r\2\2\u009c"+
		"\u009d\7g\2\2\u009d\u009e\7f\2\2\u009e\30\3\2\2\2\u009f\u00a0\7u\2\2\u00a0"+
		"\u00a1\7v\2\2\u00a1\u00a2\7c\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4\7k\2\2"+
		"\u00a4\u00a5\7e\2\2\u00a5\32\3\2\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8\7"+
		"v\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa\7o\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac"+
		"\7e\2\2\u00ac\34\3\2\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7w\2\2\u00af\u00b0"+
		"\7n\2\2\u00b0\u00b1\7n\2\2\u00b1\36\3\2\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4"+
		"\7t\2\2\u00b4\u00b5\7w\2\2\u00b5\u00b6\7g\2\2\u00b6 \3\2\2\2\u00b7\u00b8"+
		"\7h\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb\7u\2\2\u00bb"+
		"\u00bc\7g\2\2\u00bc\"\3\2\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7p\2\2\u00bf"+
		"\u00c0\7{\2\2\u00c0$\3\2\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7w\2\2\u00c3"+
		"\u00c4\7o\2\2\u00c4\u00c5\7d\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7\7t\2\2"+
		"\u00c7&\3\2\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb\7t\2"+
		"\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7i\2\2\u00ce(\3\2"+
		"\2\2\u00cf\u00d0\7d\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3"+
		"\7n\2\2\u00d3*\3\2\2\2\u00d4\u00d5\7h\2\2\u00d5\u00d6\7w\2\2\u00d6\u00d7"+
		"\7p\2\2\u00d7\u00d8\7e\2\2\u00d8\u00d9\7v\2\2\u00d9\u00da\7q\2\2\u00da"+
		"\u00db\7t\2\2\u00db,\3\2\2\2\u00dc\u00dd\7d\2\2\u00dd\u00de\7n\2\2\u00de"+
		"\u00df\7q\2\2\u00df\u00e0\7e\2\2\u00e0\u00e1\7m\2\2\u00e1.\3\2\2\2\u00e2"+
		"\u00e3\7k\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7v\2\2\u00e5\60\3\2\2\2\u00e6"+
		"\u00e7\7t\2\2\u00e7\u00e8\7g\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea\7n\2\2"+
		"\u00ea\62\3\2\2\2\u00eb\u00ec\7e\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7"+
		"o\2\2\u00ee\u00ef\7r\2\2\u00ef\u00f0\7n\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2"+
		"\7z\2\2\u00f2\64\3\2\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6"+
		"\7t\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7{\2\2\u00f8\66\3\2\2\2\u00f9\u00fa"+
		"\7o\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7t\2\2\u00fd"+
		"\u00fe\7k\2\2\u00fe\u00ff\7z\2\2\u00ff8\3\2\2\2\u0100\u0101\7n\2\2\u0101"+
		"\u0102\7k\2\2\u0102\u0103\7u\2\2\u0103\u0104\7v\2\2\u0104:\3\2\2\2\u0105"+
		"\u0106\7f\2\2\u0106\u0107\7k\2\2\u0107\u0108\7e\2\2\u0108\u0109\7v\2\2"+
		"\u0109<\3\2\2\2\u010a\u010f\5A!\2\u010b\u010f\5C\"\2\u010c\u010f\5E#\2"+
		"\u010d\u010f\5G$\2\u010e\u010a\3\2\2\2\u010e\u010b\3\2\2\2\u010e\u010c"+
		"\3\2\2\2\u010e\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\b\37\2\2"+
		"\u0111>\3\2\2\2\u0112\u0114\t\2\2\2\u0113\u0112\3\2\2\2\u0114\u0115\3"+
		"\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116@\3\2\2\2\u0117\u0119"+
		"\t\3\2\2\u0118\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u0118\3\2\2\2\u011a"+
		"\u011b\3\2\2\2\u011bB\3\2\2\2\u011c\u011d\7\61\2\2\u011d\u011e\7\61\2"+
		"\2\u011e\u0122\3\2\2\2\u011f\u0121\n\2\2\2\u0120\u011f\3\2\2\2\u0121\u0124"+
		"\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u012f\3\2\2\2\u0124"+
		"\u0122\3\2\2\2\u0125\u0126\7%\2\2\u0126\u0127\7\"\2\2\u0127\u012b\3\2"+
		"\2\2\u0128\u012a\n\4\2\2\u0129\u0128\3\2\2\2\u012a\u012d\3\2\2\2\u012b"+
		"\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2"+
		"\2\2\u012e\u011c\3\2\2\2\u012e\u0125\3\2\2\2\u012fD\3\2\2\2\u0130\u0131"+
		"\7\61\2\2\u0131\u0132\7,\2\2\u0132\u0136\3\2\2\2\u0133\u0135\13\2\2\2"+
		"\u0134\u0133\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0137\3\2\2\2\u0136\u0134"+
		"\3\2\2\2\u0137\u0139\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u013a\7,\2\2\u013a"+
		"\u0149\7\61\2\2\u013b\u013c\7b\2\2\u013c\u013d\7b\2\2\u013d\u013e\7b\2"+
		"\2\u013e\u0142\3\2\2\2\u013f\u0141\13\2\2\2\u0140\u013f\3\2\2\2\u0141"+
		"\u0144\3\2\2\2\u0142\u0143\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0145\3\2"+
		"\2\2\u0144\u0142\3\2\2\2\u0145\u0146\7b\2\2\u0146\u0147\7b\2\2\u0147\u0149"+
		"\7b\2\2\u0148\u0130\3\2\2\2\u0148\u013b\3\2\2\2\u0149F\3\2\2\2\u014a\u014c"+
		"\7^\2\2\u014b\u014d\7\17\2\2\u014c\u014b\3\2\2\2\u014c\u014d\3\2\2\2\u014d"+
		"\u014e\3\2\2\2\u014e\u014f\7\f\2\2\u014fH\3\2\2\2\u0150\u0151\7)\2\2\u0151"+
		"\u0152\7)\2\2\u0152\u0153\7)\2\2\u0153\u0157\3\2\2\2\u0154\u0156\13\2"+
		"\2\2\u0155\u0154\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0158\3\2\2\2\u0157"+
		"\u0155\3\2\2\2\u0158\u015a\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015b\7)"+
		"\2\2\u015b\u015c\7)\2\2\u015c\u016b\7)\2\2\u015d\u015e\7$\2\2\u015e\u015f"+
		"\7$\2\2\u015f\u0160\7$\2\2\u0160\u0164\3\2\2\2\u0161\u0163\13\2\2\2\u0162"+
		"\u0161\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0165\3\2\2\2\u0164\u0162\3\2"+
		"\2\2\u0165\u0167\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168\7$\2\2\u0168"+
		"\u0169\7$\2\2\u0169\u016b\7$\2\2\u016a\u0150\3\2\2\2\u016a\u015d\3\2\2"+
		"\2\u016bJ\3\2\2\2\u016c\u0170\t\5\2\2\u016d\u016f\t\6\2\2\u016e\u016d"+
		"\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171"+
		"L\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u017b\7b\2\2\u0174\u0175\7^\2\2\u0175"+
		"\u017a\7b\2\2\u0176\u0177\7^\2\2\u0177\u017a\7^\2\2\u0178\u017a\13\2\2"+
		"\2\u0179\u0174\3\2\2\2\u0179\u0176\3\2\2\2\u0179\u0178\3\2\2\2\u017a\u017d"+
		"\3\2\2\2\u017b\u017c\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017e\3\2\2\2\u017d"+
		"\u017b\3\2\2\2\u017e\u017f\7b\2\2\u017fN\3\2\2\2\u0180\u0188\7$\2\2\u0181"+
		"\u0182\7^\2\2\u0182\u0187\7$\2\2\u0183\u0184\7^\2\2\u0184\u0187\7^\2\2"+
		"\u0185\u0187\13\2\2\2\u0186\u0181\3\2\2\2\u0186\u0183\3\2\2\2\u0186\u0185"+
		"\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0189\3\2\2\2\u0188\u0186\3\2\2\2\u0189"+
		"\u018b\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u0199\7$\2\2\u018c\u0194\7)\2"+
		"\2\u018d\u018e\7^\2\2\u018e\u0193\7)\2\2\u018f\u0190\7^\2\2\u0190\u0193"+
		"\7^\2\2\u0191\u0193\13\2\2\2\u0192\u018d\3\2\2\2\u0192\u018f\3\2\2\2\u0192"+
		"\u0191\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0195\3\2\2\2\u0194\u0192\3\2"+
		"\2\2\u0195\u0197\3\2\2\2\u0196\u0194\3\2\2\2\u0197\u0199\7)\2\2\u0198"+
		"\u0180\3\2\2\2\u0198\u018c\3\2\2\2\u0199P\3\2\2\2\u019a\u019b\7h\2\2\u019b"+
		"\u019c\5O(\2\u019cR\3\2\2\2\u019d\u01a3\5W,\2\u019e\u01a3\5Y-\2\u019f"+
		"\u01a3\5[.\2\u01a0\u01a3\5]/\2\u01a1\u01a3\5c\62\2\u01a2\u019d\3\2\2\2"+
		"\u01a2\u019e\3\2\2\2\u01a2\u019f\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a1"+
		"\3\2\2\2\u01a3T\3\2\2\2\u01a4\u01a7\5_\60\2\u01a5\u01a7\5a\61\2\u01a6"+
		"\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7V\3\2\2\2\u01a8\u01aa\t\7\2\2"+
		"\u01a9\u01a8\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01b3\3\2\2\2\u01ab\u01af"+
		"\t\b\2\2\u01ac\u01ae\t\t\2\2\u01ad\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af"+
		"\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b4\3\2\2\2\u01b1\u01af\3\2"+
		"\2\2\u01b2\u01b4\7\62\2\2\u01b3\u01ab\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4"+
		"X\3\2\2\2\u01b5\u01b7\t\7\2\2\u01b6\u01b5\3\2\2\2\u01b6\u01b7\3\2\2\2"+
		"\u01b7\u01b8\3\2\2\2\u01b8\u01ba\7\62\2\2\u01b9\u01bb\t\n\2\2\u01ba\u01b9"+
		"\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd"+
		"Z\3\2\2\2\u01be\u01c0\t\7\2\2\u01bf\u01be\3\2\2\2\u01bf\u01c0\3\2\2\2"+
		"\u01c0\u01c1\3\2\2\2\u01c1\u01c2\7\62\2\2\u01c2\u01c3\7z\2\2\u01c3\u01c5"+
		"\3\2\2\2\u01c4\u01c6\t\13\2\2\u01c5\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2"+
		"\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\\\3\2\2\2\u01c9\u01cb\t"+
		"\7\2\2\u01ca\u01c9\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc"+
		"\u01cd\7\62\2\2\u01cd\u01ce\7d\2\2\u01ce\u01d0\3\2\2\2\u01cf\u01d1\t\f"+
		"\2\2\u01d0\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2"+
		"\u01d3\3\2\2\2\u01d3^\3\2\2\2\u01d4\u01d6\t\7\2\2\u01d5\u01d4\3\2\2\2"+
		"\u01d5\u01d6\3\2\2\2\u01d6\u01d8\3\2\2\2\u01d7\u01d9\t\t\2\2\u01d8\u01d7"+
		"\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db"+
		"\u01dc\3\2\2\2\u01dc\u01de\7\60\2\2\u01dd\u01df\t\t\2\2\u01de\u01dd\3"+
		"\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1"+
		"`\3\2\2\2\u01e2\u01e3\5_\60\2\u01e3\u01e4\5e\63\2\u01e4b\3\2\2\2\u01e5"+
		"\u01e6\5W,\2\u01e6\u01e7\5e\63\2\u01e7d\3\2\2\2\u01e8\u01ea\t\r\2\2\u01e9"+
		"\u01eb\t\7\2\2\u01ea\u01e9\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ed\3\2"+
		"\2\2\u01ec\u01ee\t\t\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef"+
		"\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0f\3\2\2\2(\2\u010e\u0115\u011a"+
		"\u0122\u012b\u012e\u0136\u0142\u0148\u014c\u0157\u0164\u016a\u0170\u0179"+
		"\u017b\u0186\u0188\u0192\u0194\u0198\u01a2\u01a6\u01a9\u01af\u01b3\u01b6"+
		"\u01bc\u01bf\u01c7\u01ca\u01d2\u01d5\u01da\u01e0\u01ea\u01ef\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}