import sys

def main() -> None:
    """
    ICSI254 - AAD Problems (2026 Spring)
    Problem: daraalal

   What you must do:
    - Read input from STDIN
    - Print the answer to STDOUT
    - Do NOT print extra debug text

    Input format:
    N K
    A1 A2 ... AN
    B1 B2 ... BN

    Output:
    - One integer: the minimum possible value

    Notes:
    - Auto-tests are in: daraalal/test/*.in and *.out
    - Local test command: python daraalal/run_test.py
    """

    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)

    N = int(next(it))
    K = int(next(it))

    A = [int(next(it)) for _ in range(N)]
    B = [int(next(it)) for _ in range(N)]

    # TODO: Implement your solution here.
    # Remove the line below after implementing.
    print(0)

if __name__ == "__main__":
    main()
