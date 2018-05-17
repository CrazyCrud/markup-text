def generate_normalized_text(input):
    for line in input:
        yield line
    yield "\n"


def blocks(input_file):
    block = []
    for line in generate_normalized_text(input_file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
