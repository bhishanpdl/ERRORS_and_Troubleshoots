# ref: https://pypi.org/project/jq/

# test 01
import jq

assert jq.compile(".+5").input_value(42).first() == 47

# test 02
assert jq.compile(".").input_value(None).first() == None
assert jq.compile(".").input_value(42).first() == 42
assert jq.compile(".").input_value(0.42).first() == 0.42
assert jq.compile(".").input_value(True).first() == True
assert jq.compile(".").input_value("hello").first() == "hello"

# test 03
assert jq.compile(".+5").input_values([1, 2, 3]).all() == [6, 7, 8]

# test 04
assert jq.compile(".").input_text("null").first() == None
assert jq.compile(".").input_text("42").first() == 42
assert jq.compile(".").input_text("0.42").first() == 0.42
assert jq.compile(".").input_text("true").first() == True
assert jq.compile(".").input_text('"hello"').first() == "hello"
assert jq.compile(".").input_text("1\n2\n3").all() == [1, 2, 3]

# test 05
assert jq.compile(".").input_text("1\n2\n3", slurp=True).first() == [1, 2, 3]

# test 06
assert jq.compile(".").input("hello").first() == "hello"
assert jq.compile(".").input(text='"hello"').first() == "hello"

# test 07
assert jq.compile(".").input_value("hello").first() == "hello"
assert jq.compile("[.[]+1]").input_value([1, 2, 3]).first() == [2, 3, 4]
assert jq.compile(".[]+1").input_value([1, 2, 3]).first() == 2

# test 08
assert jq.compile(".").input_value("42").text() == '"42"'
assert jq.compile(".[]").input_value([1, 2, 3]).text() == "1\n2\n3"
assert jq.compile(".[]+1").input_value([1, 2, 3]).all() == [2, 3, 4]

iterator = iter(jq.compile(".[]+1").input_value([1, 2, 3]))
assert next(iterator, None) == 2
assert next(iterator, None) == 3
assert next(iterator, None) == 4
assert next(iterator, None) == None

# test 09
program = jq.compile("$a + $b + .", args={"a": 100, "b": 20})
assert program.input_value(3).first() == 123

# test 10
assert jq.first(".[] + 1", [1, 2, 3]) == 2
assert jq.first(".[] + 1", text="[1, 2, 3]") == 2
assert jq.text(".[] + 1", [1, 2, 3]) == "2\n3\n4"
assert jq.all(".[] + 1", [1, 2, 3]) == [2, 3, 4]
assert list(jq.iter(".[] + 1", [1, 2, 3])) == [2, 3, 4]
