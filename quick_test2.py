from sgffp.cli import _open_input
import glob

for file in glob.glob("degenerate_examples/*.dna"):

    sgff = _open_input(file)
    child_sequence = sgff.blocks[0][0]["sequence"]
    parent_sequence = sgff.history.get_sequence_at(0)
    print(parent_sequence)
    print(child_sequence)
    print(parent_sequence == child_sequence)
