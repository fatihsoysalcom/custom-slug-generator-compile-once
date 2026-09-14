import re
import unicodedata

def generate_slug(text):
    """
    Generates a URL-friendly slug from a given text.
    This function represents a 'compile once' solution:
    instead of relying on a third-party service or library for a simple task,
    you build and own this utility once, then reuse it freely.
    """
    # Normalize Unicode characters (e.g., 'ş' -> 's', 'ç' -> 'c')
    # This helps in handling international characters gracefully, including Turkish ones.
    text = str(text)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

    # Convert to lowercase
    text = text.lower()

    # Replace non-alphanumeric characters (except hyphens) with a hyphen
    text = re.sub(r'[^\w\s-]', '', text)

    # Replace spaces with hyphens
    text = re.sub(r'[\s]+', '-', text)

    # Remove leading/trailing hyphens
    text = text.strip('-')

    # Collapse multiple hyphens into a single hyphen
    text = re.sub(r'[-]+', '-', text)

    return text

if __name__ == "__main__":
    print("--- Slug Generator (Compile Once Example) ---")
    print("This script demonstrates building a reusable utility once,")
    print("rather than repeatedly paying for or relying on external services for simple tasks.")
    print("-" * 40)

    # Example usage with Turkish characters, illustrating the 'compile once' principle
    # You write this utility once, and it serves your needs indefinitely without external costs.
    title1 = "Tekrar Tekrar Ödeme Yapmaktan Kurtulun: Kendi Yapınızı Bir Kez Derleyin!"
    slug1 = generate_slug(title1)
    print(f"Original: '{title1}'")
    print(f"Slug:     '{slug1}'\n")

    title2 = "CapCut Geceleri Neden Bize Pahalıya Mal Oluyor?"
    slug2 = generate_slug(title2)
    print(f"Original: '{title2}'")
    print(f"Slug:     '{slug2}'\n")

    title3 = "Dijital Altyapınızı Optimize Edin ve Verimli Hale Getirin!"
    slug3 = generate_slug(title3)
    print(f"Original: '{title3}'")
    print(f"Slug:     '{slug3}'\n")

    title4 = "  Hello World! This is a test string with special chars: @#$%"
    slug4 = generate_slug(title4)
    print(f"Original: '{title4}'")
    print(f"Slug:     '{slug4}'\n")

    print("---------------------------------------------")
    print("By 'compiling' (writing) this utility once, you gain full control,")
    print("avoid recurring costs, and ensure long-term reusability.")