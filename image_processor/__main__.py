import argparse
from .core import to_grayscale, blur

def main():
    parser = argparse.ArgumentParser(description="Image Processor CLI")
    parser.add_argument("action", choices=["grayscale", "blur"])
    parser.add_argument("input", help="Caminho da imagem de entrada")
    parser.add_argument("output", help="Caminho da imagem de saída")
    parser.add_argument("--radius", type=int, default=2, help="Raio do blur (se aplicável)")

    args = parser.parse_args()

    if args.action == "grayscale":
        to_grayscale(args.input, args.output)
    elif args.action == "blur":
        blur(args.input, args.output, args.radius)

if __name__ == "__main__":
    main()
