import numpy as np
from math import log2, ceil
import pandas as pd

def generate_sequence(N):
    """Generate a random sequence with given probabilities."""
    symbols = ['a', 'b', 'c', 'd']
    probabilities = [0.5, 0.25, 0.2, 0.05]
    return ''.join(np.random.choice(symbols, size=N, p=probabilities))

def calculate_entropy():
    """Calculate source entropy in bits/symbol."""
    probabilities = {'a': 0.5, 'b': 0.25, 'c': 0.2, 'd': 0.05}
    return -sum(p * log2(p) for p in probabilities.values() if p > 0)

def lz78_encode(data):
    """Implement LZ78 encoding, returning encoded packets and dictionary."""
    dictionary = {0: ''}
    next_code = 1
    current_phrase = ''
    encoded = []

    for symbol in data:
        current_phrase += symbol
        if current_phrase not in dictionary.values():
            prefix = current_phrase[:-1]
            prefix_code = [k for k, v in dictionary.items() if v == prefix][0]
            dictionary[next_code] = current_phrase
            encoded.append((prefix_code, symbol))
            next_code += 1
            current_phrase = ''

    if current_phrase:
        prefix = current_phrase[:-1]
        prefix_code = [k for k, v in dictionary.items() if v == prefix][0]
        encoded.append((prefix_code, current_phrase[-1]))

    return encoded, dictionary

def calculate_encoded_bits(encoded_sequence):
    """Calculate total bits required for encoding."""
    total_bits = 0
    for code, symbol in encoded_sequence:
        code_bits = 1 if code == 0 else ceil(log2(code + 1))
        symbol_bits = 8  # ASCII encoding
        total_bits += code_bits + symbol_bits
    return total_bits

def create_detailed_table(encoded_sequence, dictionary):
    """Create detailed table for encoded phrases."""
    table = []
    for i, (code, symbol) in enumerate(encoded_sequence, 1):
        phrase = dictionary.get(i, '')
        transmitted_code = f"{bin(code)[2:]}{ord(symbol):08b}"
        table.append({
            'Phrase Address': i,
            'Dictionary Content': phrase,
            'Encoded Packets': f"({code}, {symbol})",
            'Transmitted Code': transmitted_code
        })
    return pd.DataFrame(table)

def run_experiments(sequence_lengths):
    """Run experiments for different sequence lengths."""
    results = []
    for N in sequence_lengths:
        sequence = generate_sequence(N)
        encoded, dictionary = lz78_encode(sequence)
        encoded_bits = calculate_encoded_bits(encoded)
        compression_ratio = encoded_bits / (8 * N)
        bits_per_symbol = encoded_bits / N

        results.append({
            'N': N,
            'N_B': encoded_bits,
            'Compression Ratio': compression_ratio,
            'Bits per Symbol': bits_per_symbol,
            'Sequence': sequence,
            'Encoded': encoded,
            'Dictionary': dictionary
        })
    return results

def main():
    """Main function to execute experiments and display results."""
    # Calculate entropy
    entropy = calculate_entropy()
    print(f"Source entropy H = {entropy:.4f} bits/symbol\n")

    # Define sequence lengths
    sequence_lengths = [20, 50, 100, 200, 400, 800, 1000, 5000]

    # Run experiments
    results = run_experiments(sequence_lengths)

    # Display summary table
    summary_table = pd.DataFrame([{
        'N': r['N'],
        'N_B': r['N_B'],
        'Compression Ratio': f"{r['Compression Ratio']:.4f}",
        'Bits per Symbol': f"{r['Bits per Symbol']:.4f}"
    } for r in results])
    print("Summary Table:")
    print(summary_table.to_string(index=False))  # Use to_string() instead of to_markdown()

    # Display detailed table for N=20
    n20_result = next(r for r in results if r['N'] == 20)
    detailed_table = create_detailed_table(n20_result['Encoded'], n20_result['Dictionary'])
    print("\nDetailed Table for N=20:")
    print(detailed_table.to_string(index=False))

if __name__ == "__main__":
    main()