
import argparse
import pandas as pd
from pathlib import Path

def summarize_dataframe(df: pd.DataFrame, max_examples: int = 3) -> str:
    lines = [
        "=== Dataset Overview ===",
        f"Rows: {len(df)}",
        f"Columns: {len(df.columns)}",
        "",
        "=== Missing Values by Column ==="
    ]
    for col, val in df.isna().sum().sort_values(ascending=False).items():
        lines.append(f"{col}: {val}")
    lines.append("")
    lines.append("=== Column Summary ===")
    for col in df.columns:
        s = df[col]
        dtype = s.dtype
        examples = s.dropna().unique()[:max_examples]
        lines.append(f"- {col}")
        lines.append(f"  dtype: {dtype}")
        lines.append(f"  missing: {s.isna().sum()}")
        lines.append(f"  unique: {s.nunique(dropna=True)}")
        lines.append(f"  examples: {', '.join(map(str, examples))}")
    return "\n".join(lines)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", default="data/sample.csv", help="Path to CSV file")
    args = p.parse_args()
    path = Path(args.csv)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path.resolve()}")
    df = pd.read_csv(path)
    print(summarize_dataframe(df))

if __name__ == "__main__":
    main()
