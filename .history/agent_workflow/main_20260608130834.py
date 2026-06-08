import sys
from workflow import run_workflow


def main(argv=None):
    argv = argv or sys.argv[1:]
    if argv:
        prompt = " ".join(argv)
    else:
        prompt = input("Enter a prompt: ").strip()

    final = run_workflow(prompt)
    # Final workflow output is plain text containing the refined content
    print(final)


if __name__ == "__main__":
    main()
