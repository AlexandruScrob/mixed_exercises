import libcst as cst
from libcst.metadata import PositionProvider


# Purpose of match statement is for matching of the object structure and not necessarily
# for the switch cases
class Visitor(cst.CSTVisitor):
    METADATA_DEPENDENCIES = (PositionProvider,)

    def visit_Tuple(self, node: cst.Tuple):
        pos = self.get_metadata(PositionProvider, node)

        if pos.start.line != pos.end.line:
            return

        match node:
            case cst.Tuple(
                elements=[
                    *_,
                    _,
                    cst.Element(
                        value=cst.Comparison(
                            comparisons=[
                                cst.ComparisonTarget(
                                    operator=cst.Equal(), comparator=cst.Tuple() as tup
                                ),
                            ],
                            lpar=[],
                            rpar=[],
                        ),
                    ),
                ],
            ):
                pos = self.get_metadata(PositionProvider, tup)
                print(f"matched {pos.start.line, pos.start.column}")


def ambiguous_tuple_equality_example():
    codes = [
        "True, True, True == (True, True, True)",
        "True, True, (True == (True, True, True))",
        "(True, True, True) == (True, True, True)",
    ]

    for code in codes:
        print(code)
        node = cst.parse_module(code)
        node_with_metadata = cst.MetadataWrapper(node)
        # print(dump(node.body[0].body[0].value, show_syntax=True, indent=" " * 4, show_whitespace=True, show_defaults=True))
        node_with_metadata.visit(Visitor())


if __name__ == "__main__":
    ambiguous_tuple_equality_example()
