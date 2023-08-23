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
		IDENTIFIER=33, UNIT=34, STRING=35, FSTRING=36, COMPLEX=37, INTEGER=38, 
		REAL=39, DECIMAL_INTEGER=40;
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
			"LINE_MID", "MULTI_STR", "IDENTIFIER", "UNIT", "STRING", "FSTRING", "COMPLEX", 
			"INTEGER", "REAL", "DECIMAL_INTEGER", "POINT_FLOAT", "EXPONENT_FLOAT", 
			"NON_ZERO_DIGIT", "DIGIT", "INT_PART", "FRACTION", "EXPONENT"
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
			"UNIT", "STRING", "FSTRING", "COMPLEX", "INTEGER", "REAL", "DECIMAL_INTEGER"
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*\u01e2\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3"+
		"\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f"+
		"\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3"+
		"\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3"+
		"\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3"+
		"\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3"+
		"\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3"+
		"\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3"+
		"\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3"+
		"\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3"+
		"\37\3\37\3\37\5\37\u0111\n\37\3\37\3\37\3 \6 \u0116\n \r \16 \u0117\3"+
		"!\6!\u011b\n!\r!\16!\u011c\3\"\3\"\3\"\3\"\7\"\u0123\n\"\f\"\16\"\u0126"+
		"\13\"\3\"\3\"\3\"\3\"\7\"\u012c\n\"\f\"\16\"\u012f\13\"\5\"\u0131\n\""+
		"\3#\3#\3#\3#\7#\u0137\n#\f#\16#\u013a\13#\3#\3#\3#\3#\3#\3#\3#\7#\u0143"+
		"\n#\f#\16#\u0146\13#\3#\3#\3#\5#\u014b\n#\3$\3$\5$\u014f\n$\3$\3$\3%\3"+
		"%\3%\3%\3%\7%\u0158\n%\f%\16%\u015b\13%\3%\3%\3%\3%\3%\3%\3%\3%\7%\u0165"+
		"\n%\f%\16%\u0168\13%\3%\3%\3%\5%\u016d\n%\3&\3&\7&\u0171\n&\f&\16&\u0174"+
		"\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u017c\n\'\f\'\16\'\u017f\13\'\3\'\3\'"+
		"\3(\3(\3(\3(\3(\3(\7(\u0189\n(\f(\16(\u018c\13(\3(\3(\3(\3(\3(\3(\3(\7"+
		"(\u0195\n(\f(\16(\u0198\13(\3(\5(\u019b\n(\3)\3)\3)\3*\3*\3*\3*\3*\3*"+
		"\3*\3*\3*\3*\5*\u01aa\n*\3+\3+\3,\3,\5,\u01b0\n,\3-\3-\7-\u01b4\n-\f-"+
		"\16-\u01b7\13-\3-\6-\u01ba\n-\r-\16-\u01bb\5-\u01be\n-\3.\3.\3.\5.\u01c3"+
		"\n.\3/\3/\5/\u01c7\n/\3/\3/\3\60\3\60\3\61\3\61\3\62\6\62\u01d0\n\62\r"+
		"\62\16\62\u01d1\3\63\3\63\6\63\u01d6\n\63\r\63\16\63\u01d7\3\64\3\64\5"+
		"\64\u01dc\n\64\3\64\6\64\u01df\n\64\r\64\16\64\u01e0\t\u0138\u0144\u0159"+
		"\u0166\u017d\u018a\u0196\2\65\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13"+
		"\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61"+
		"\32\63\33\65\34\67\359\36;\37= ?!A\2C\2E\2G\2I\"K#M$O%Q&S\'U(W)Y*[\2]"+
		"\2_\2a\2c\2e\2g\2\3\2\13\4\2\f\f\17\17\5\2\13\13\16\16\"\"\4\2\f\f\16"+
		"\17\5\2C\\aac|\6\2\62;C\\aac|\4\2--//\3\2\63;\3\2\62;\4\2GGgg\2\u01fb"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2"+
		"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2"+
		"\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3"+
		"\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2"+
		"\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\3i\3\2\2\2\5"+
		"l\3\2\2\2\7p\3\2\2\2\tt\3\2\2\2\13y\3\2\2\2\r~\3\2\2\2\17\u0083\3\2\2"+
		"\2\21\u0088\3\2\2\2\23\u008f\3\2\2\2\25\u0095\3\2\2\2\27\u009a\3\2\2\2"+
		"\31\u00a1\3\2\2\2\33\u00a8\3\2\2\2\35\u00af\3\2\2\2\37\u00b4\3\2\2\2!"+
		"\u00b9\3\2\2\2#\u00bf\3\2\2\2%\u00c3\3\2\2\2\'\u00ca\3\2\2\2)\u00d1\3"+
		"\2\2\2+\u00d6\3\2\2\2-\u00de\3\2\2\2/\u00e4\3\2\2\2\61\u00e8\3\2\2\2\63"+
		"\u00ed\3\2\2\2\65\u00f5\3\2\2\2\67\u00fb\3\2\2\29\u0102\3\2\2\2;\u0107"+
		"\3\2\2\2=\u0110\3\2\2\2?\u0115\3\2\2\2A\u011a\3\2\2\2C\u0130\3\2\2\2E"+
		"\u014a\3\2\2\2G\u014c\3\2\2\2I\u016c\3\2\2\2K\u016e\3\2\2\2M\u0175\3\2"+
		"\2\2O\u019a\3\2\2\2Q\u019c\3\2\2\2S\u01a9\3\2\2\2U\u01ab\3\2\2\2W\u01af"+
		"\3\2\2\2Y\u01bd\3\2\2\2[\u01bf\3\2\2\2]\u01c6\3\2\2\2_\u01ca\3\2\2\2a"+
		"\u01cc\3\2\2\2c\u01cf\3\2\2\2e\u01d3\3\2\2\2g\u01d9\3\2\2\2ij\7c\2\2j"+
		"k\7u\2\2k\4\3\2\2\2lm\7n\2\2mn\7g\2\2no\7v\2\2o\6\3\2\2\2pq\7w\2\2qr\7"+
		"u\2\2rs\7g\2\2s\b\3\2\2\2tu\7h\2\2uv\7w\2\2vw\7p\2\2wx\7e\2\2x\n\3\2\2"+
		"\2yz\7v\2\2z{\7{\2\2{|\7r\2\2|}\7g\2\2}\f\3\2\2\2~\177\7g\2\2\177\u0080"+
		"\7p\2\2\u0080\u0081\7w\2\2\u0081\u0082\7o\2\2\u0082\16\3\2\2\2\u0083\u0084"+
		"\7y\2\2\u0084\u0085\7k\2\2\u0085\u0086\7v\2\2\u0086\u0087\7j\2\2\u0087"+
		"\20\3\2\2\2\u0088\u0089\7t\2\2\u0089\u008a\7g\2\2\u008a\u008b\7v\2\2\u008b"+
		"\u008c\7w\2\2\u008c\u008d\7t\2\2\u008d\u008e\7p\2\2\u008e\22\3\2\2\2\u008f"+
		"\u0090\7k\2\2\u0090\u0091\7p\2\2\u0091\u0092\7p\2\2\u0092\u0093\7g\2\2"+
		"\u0093\u0094\7t\2\2\u0094\24\3\2\2\2\u0095\u0096\7u\2\2\u0096\u0097\7"+
		"{\2\2\u0097\u0098\7p\2\2\u0098\u0099\7e\2\2\u0099\26\3\2\2\2\u009a\u009b"+
		"\7u\2\2\u009b\u009c\7e\2\2\u009c\u009d\7q\2\2\u009d\u009e\7r\2\2\u009e"+
		"\u009f\7g\2\2\u009f\u00a0\7f\2\2\u00a0\30\3\2\2\2\u00a1\u00a2\7u\2\2\u00a2"+
		"\u00a3\7v\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5\7v\2\2\u00a5\u00a6\7k\2\2"+
		"\u00a6\u00a7\7e\2\2\u00a7\32\3\2\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa\7"+
		"v\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7o\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae"+
		"\7e\2\2\u00ae\34\3\2\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7w\2\2\u00b1\u00b2"+
		"\7n\2\2\u00b2\u00b3\7n\2\2\u00b3\36\3\2\2\2\u00b4\u00b5\7v\2\2\u00b5\u00b6"+
		"\7t\2\2\u00b6\u00b7\7w\2\2\u00b7\u00b8\7g\2\2\u00b8 \3\2\2\2\u00b9\u00ba"+
		"\7h\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc\7n\2\2\u00bc\u00bd\7u\2\2\u00bd"+
		"\u00be\7g\2\2\u00be\"\3\2\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1\7p\2\2\u00c1"+
		"\u00c2\7{\2\2\u00c2$\3\2\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7w\2\2\u00c5"+
		"\u00c6\7o\2\2\u00c6\u00c7\7d\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7t\2\2"+
		"\u00c9&\3\2\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7t\2"+
		"\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0\7i\2\2\u00d0(\3\2"+
		"\2\2\u00d1\u00d2\7d\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5"+
		"\7n\2\2\u00d5*\3\2\2\2\u00d6\u00d7\7h\2\2\u00d7\u00d8\7w\2\2\u00d8\u00d9"+
		"\7p\2\2\u00d9\u00da\7e\2\2\u00da\u00db\7v\2\2\u00db\u00dc\7q\2\2\u00dc"+
		"\u00dd\7t\2\2\u00dd,\3\2\2\2\u00de\u00df\7d\2\2\u00df\u00e0\7n\2\2\u00e0"+
		"\u00e1\7q\2\2\u00e1\u00e2\7e\2\2\u00e2\u00e3\7m\2\2\u00e3.\3\2\2\2\u00e4"+
		"\u00e5\7k\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7v\2\2\u00e7\60\3\2\2\2\u00e8"+
		"\u00e9\7t\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7n\2\2"+
		"\u00ec\62\3\2\2\2\u00ed\u00ee\7e\2\2\u00ee\u00ef\7q\2\2\u00ef\u00f0\7"+
		"o\2\2\u00f0\u00f1\7r\2\2\u00f1\u00f2\7n\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4"+
		"\7z\2\2\u00f4\64\3\2\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8"+
		"\7t\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa\7{\2\2\u00fa\66\3\2\2\2\u00fb\u00fc"+
		"\7o\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7t\2\2\u00ff"+
		"\u0100\7k\2\2\u0100\u0101\7z\2\2\u01018\3\2\2\2\u0102\u0103\7n\2\2\u0103"+
		"\u0104\7k\2\2\u0104\u0105\7u\2\2\u0105\u0106\7v\2\2\u0106:\3\2\2\2\u0107"+
		"\u0108\7f\2\2\u0108\u0109\7k\2\2\u0109\u010a\7e\2\2\u010a\u010b\7v\2\2"+
		"\u010b<\3\2\2\2\u010c\u0111\5A!\2\u010d\u0111\5C\"\2\u010e\u0111\5E#\2"+
		"\u010f\u0111\5G$\2\u0110\u010c\3\2\2\2\u0110\u010d\3\2\2\2\u0110\u010e"+
		"\3\2\2\2\u0110\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\b\37\2\2"+
		"\u0113>\3\2\2\2\u0114\u0116\t\2\2\2\u0115\u0114\3\2\2\2\u0116\u0117\3"+
		"\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118@\3\2\2\2\u0119\u011b"+
		"\t\3\2\2\u011a\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011a\3\2\2\2\u011c"+
		"\u011d\3\2\2\2\u011dB\3\2\2\2\u011e\u011f\7\61\2\2\u011f\u0120\7\61\2"+
		"\2\u0120\u0124\3\2\2\2\u0121\u0123\n\2\2\2\u0122\u0121\3\2\2\2\u0123\u0126"+
		"\3\2\2\2\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0131\3\2\2\2\u0126"+
		"\u0124\3\2\2\2\u0127\u0128\7%\2\2\u0128\u0129\7\"\2\2\u0129\u012d\3\2"+
		"\2\2\u012a\u012c\n\4\2\2\u012b\u012a\3\2\2\2\u012c\u012f\3\2\2\2\u012d"+
		"\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0131\3\2\2\2\u012f\u012d\3\2"+
		"\2\2\u0130\u011e\3\2\2\2\u0130\u0127\3\2\2\2\u0131D\3\2\2\2\u0132\u0133"+
		"\7\61\2\2\u0133\u0134\7,\2\2\u0134\u0138\3\2\2\2\u0135\u0137\13\2\2\2"+
		"\u0136\u0135\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0139\3\2\2\2\u0138\u0136"+
		"\3\2\2\2\u0139\u013b\3\2\2\2\u013a\u0138\3\2\2\2\u013b\u013c\7,\2\2\u013c"+
		"\u014b\7\61\2\2\u013d\u013e\7b\2\2\u013e\u013f\7b\2\2\u013f\u0140\7b\2"+
		"\2\u0140\u0144\3\2\2\2\u0141\u0143\13\2\2\2\u0142\u0141\3\2\2\2\u0143"+
		"\u0146\3\2\2\2\u0144\u0145\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0147\3\2"+
		"\2\2\u0146\u0144\3\2\2\2\u0147\u0148\7b\2\2\u0148\u0149\7b\2\2\u0149\u014b"+
		"\7b\2\2\u014a\u0132\3\2\2\2\u014a\u013d\3\2\2\2\u014bF\3\2\2\2\u014c\u014e"+
		"\7^\2\2\u014d\u014f\7\17\2\2\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f"+
		"\u0150\3\2\2\2\u0150\u0151\7\f\2\2\u0151H\3\2\2\2\u0152\u0153\7)\2\2\u0153"+
		"\u0154\7)\2\2\u0154\u0155\7)\2\2\u0155\u0159\3\2\2\2\u0156\u0158\13\2"+
		"\2\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2\u0159\u015a\3\2\2\2\u0159"+
		"\u0157\3\2\2\2\u015a\u015c\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015d\7)"+
		"\2\2\u015d\u015e\7)\2\2\u015e\u016d\7)\2\2\u015f\u0160\7$\2\2\u0160\u0161"+
		"\7$\2\2\u0161\u0162\7$\2\2\u0162\u0166\3\2\2\2\u0163\u0165\13\2\2\2\u0164"+
		"\u0163\3\2\2\2\u0165\u0168\3\2\2\2\u0166\u0167\3\2\2\2\u0166\u0164\3\2"+
		"\2\2\u0167\u0169\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016a\7$\2\2\u016a"+
		"\u016b\7$\2\2\u016b\u016d\7$\2\2\u016c\u0152\3\2\2\2\u016c\u015f\3\2\2"+
		"\2\u016dJ\3\2\2\2\u016e\u0172\t\5\2\2\u016f\u0171\t\6\2\2\u0170\u016f"+
		"\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173"+
		"L\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u017d\7b\2\2\u0176\u0177\7^\2\2\u0177"+
		"\u017c\7b\2\2\u0178\u0179\7^\2\2\u0179\u017c\7^\2\2\u017a\u017c\13\2\2"+
		"\2\u017b\u0176\3\2\2\2\u017b\u0178\3\2\2\2\u017b\u017a\3\2\2\2\u017c\u017f"+
		"\3\2\2\2\u017d\u017e\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u0180\3\2\2\2\u017f"+
		"\u017d\3\2\2\2\u0180\u0181\7b\2\2\u0181N\3\2\2\2\u0182\u018a\7$\2\2\u0183"+
		"\u0184\7^\2\2\u0184\u0189\7$\2\2\u0185\u0186\7^\2\2\u0186\u0189\7^\2\2"+
		"\u0187\u0189\13\2\2\2\u0188\u0183\3\2\2\2\u0188\u0185\3\2\2\2\u0188\u0187"+
		"\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u018b\3\2\2\2\u018a\u0188\3\2\2\2\u018b"+
		"\u018d\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u019b\7$\2\2\u018e\u0196\7)\2"+
		"\2\u018f\u0190\7^\2\2\u0190\u0195\7)\2\2\u0191\u0192\7^\2\2\u0192\u0195"+
		"\7^\2\2\u0193\u0195\13\2\2\2\u0194\u018f\3\2\2\2\u0194\u0191\3\2\2\2\u0194"+
		"\u0193\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0197\3\2\2\2\u0196\u0194\3\2"+
		"\2\2\u0197\u0199\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019b\7)\2\2\u019a"+
		"\u0182\3\2\2\2\u019a\u018e\3\2\2\2\u019bP\3\2\2\2\u019c\u019d\7h\2\2\u019d"+
		"\u019e\5O(\2\u019eR\3\2\2\2\u019f\u01a0\5U+\2\u01a0\u01a1\t\7\2\2\u01a1"+
		"\u01a2\5U+\2\u01a2\u01a3\7k\2\2\u01a3\u01aa\3\2\2\2\u01a4\u01a5\5W,\2"+
		"\u01a5\u01a6\t\7\2\2\u01a6\u01a7\5W,\2\u01a7\u01a8\7k\2\2\u01a8\u01aa"+
		"\3\2\2\2\u01a9\u019f\3\2\2\2\u01a9\u01a4\3\2\2\2\u01aaT\3\2\2\2\u01ab"+
		"\u01ac\5Y-\2\u01acV\3\2\2\2\u01ad\u01b0\5[.\2\u01ae\u01b0\5]/\2\u01af"+
		"\u01ad\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0X\3\2\2\2\u01b1\u01b5\5_\60\2"+
		"\u01b2\u01b4\5a\61\2\u01b3\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3"+
		"\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01be\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8"+
		"\u01ba\7\62\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01b9\3"+
		"\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01b1\3\2\2\2\u01bd"+
		"\u01b9\3\2\2\2\u01beZ\3\2\2\2\u01bf\u01c2\5c\62\2\u01c0\u01c3\5e\63\2"+
		"\u01c1\u01c3\7\60\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3\\"+
		"\3\2\2\2\u01c4\u01c7\5c\62\2\u01c5\u01c7\5[.\2\u01c6\u01c4\3\2\2\2\u01c6"+
		"\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\5g\64\2\u01c9^\3\2\2\2"+
		"\u01ca\u01cb\t\b\2\2\u01cb`\3\2\2\2\u01cc\u01cd\t\t\2\2\u01cdb\3\2\2\2"+
		"\u01ce\u01d0\5a\61\2\u01cf\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01cf"+
		"\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2d\3\2\2\2\u01d3\u01d5\7\60\2\2\u01d4"+
		"\u01d6\5a\61\2\u01d5\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d5\3\2"+
		"\2\2\u01d7\u01d8\3\2\2\2\u01d8f\3\2\2\2\u01d9\u01db\t\n\2\2\u01da\u01dc"+
		"\t\7\2\2\u01db\u01da\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd"+
		"\u01df\5a\61\2\u01de\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01de\3\2"+
		"\2\2\u01e0\u01e1\3\2\2\2\u01e1h\3\2\2\2#\2\u0110\u0117\u011c\u0124\u012d"+
		"\u0130\u0138\u0144\u014a\u014e\u0159\u0166\u016c\u0172\u017b\u017d\u0188"+
		"\u018a\u0194\u0196\u019a\u01a9\u01af\u01b5\u01bb\u01bd\u01c2\u01c6\u01d1"+
		"\u01d7\u01db\u01e0\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}