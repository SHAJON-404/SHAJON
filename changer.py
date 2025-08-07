import os

class SHAJON:
    def __init__(self):
        self.banner()
        self.run()

    def banner(self):
        os.system("clear" if os.name == "posix" else "cls")
        print("===================================")
        print("    uid|pas|cookies ==> uid|pas")
        print("       Developer: S. SHAJON")
        print("===================================")

    def run(self):
        file_path = input("Enter input file path: ").strip()
        print("===================================")
        if not os.path.isfile(file_path):
            print("[•] File not found.")
            return

        output_path = input("Enter output file name (e.g., result.txt): ").strip()
        print("===================================")
        if not output_path:
            print("[•] Invalid output filename.")
            return

        output_lines = []
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 2:
                    output_lines.append(f"{parts[0]}|{parts[1]}")

        if output_lines:
            with open(output_path, "w", encoding='utf-8') as f:
                f.write("\n".join(output_lines))
            print(f"[•] Conversion successful! Saved as: {output_path}")
            print("===================================")
        else:
            print("[•] No valid lines found in the file.")

if __name__ == "__main__":
    SHAJON()
