import unittest
from pathlib import Path
import sgffp

test_folder = Path(__file__).parent / "data"


class ExampleTest(unittest.TestCase):
    def parse_fasta(self, file_path: Path) -> dict[str, str]:
        key = ""
        out_dict = dict()
        for line in file_path.read_text().splitlines():
            if line.startswith(">"):
                key = line[1:].strip()
            else:
                out_dict[key] = line.strip()
        return out_dict

    def test_example_gibson_assembly(self):
        object = sgffp.SgffReader.from_file(test_folder / "gibson_assembly.dna")
        fasta_dict = self.parse_fasta(test_folder / "gibson_assembly.fasta")
        self.assertEqual(object.block(0)["sequence"], fasta_dict["product"])
        root_node = object.history.tree.root

        linearized_vector_tree_node, fragment_tree_node = root_node.children

        linear_vector_node = object.history.get_node(linearized_vector_tree_node.id)
        self.assertEqual(linear_vector_node.sequence, fasta_dict["linearized_vector"])

        fragment_node = object.history.get_node(fragment_tree_node.id)
        self.assertEqual(fragment_node.sequence, fasta_dict["fragment"])
