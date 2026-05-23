#!/usr/bin/env python3
"""Scan solved problems and rewrite the progress section in README.md."""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent
SOLUTIONS_DIR = REPO_ROOT / "Data Structures & Algorithms"
README = REPO_ROOT / "README.md"

# NeetCode 150 — category → problem slugs (matches folder names in repo)
CATEGORIES = {
    "Arrays & Hashing": [
        "duplicate-integer",
        "is-anagram",
        "two-integer-sum",
        "anagram-groups",
        "top-k-elements-in-list",
        "products-of-array-discluding-self",
        "valid-sudoku",
        "string-encode-and-decode",
        "longest-consecutive-sequence",
    ],
    "Two Pointers": [
        "is-palindrome",
        "two-integer-sum-ii",
        "three-integer-sum",
        "max-water-container",
        "trapping-rain-water",
    ],
    "Sliding Window": [
        "buy-and-sell-crypto",
        "longest-substring-without-duplicates",
        "longest-repeating-substring-with-replacement",
        "permutation-string",
        "minimum-window-with-characters",
        "sliding-window-maximum",
    ],
    "Stack": [
        "validate-parentheses",
        "minimum-stack",
        "evaluate-reverse-polish-notation",
        "generate-parentheses",
        "daily-temperatures",
        "car-fleet",
        "largest-rectangle-in-histogram",
    ],
    "Binary Search": [
        "binary-search",
        "search-2d-matrix",
        "eating-bananas",
        "find-minimum-in-rotated-sorted-array",
        "search-rotated-sorted-array",
        "time-based-key-value-store",
        "median-of-two-sorted-arrays",
    ],
    "Linked List": [
        "reverse-a-linked-list",
        "merge-two-sorted-linked-lists",
        "reorder-linked-list",
        "remove-node-from-end-of-linked-list",
        "copy-linked-list-with-random-pointer",
        "add-two-numbers",
        "linked-list-cycle-detection",
        "find-duplicate-number",
        "lru-cache",
        "merge-k-sorted-linked-lists",
        "reverse-nodes-in-k-group",
    ],
    "Trees": [
        "invert-a-binary-tree",
        "depth-of-binary-tree",
        "binary-tree-diameter",
        "balanced-binary-tree",
        "same-binary-tree",
        "subtree-of-a-binary-tree",
        "lowest-common-ancestor-in-binary-search-tree",
        "level-order-traversal-of-binary-tree",
        "binary-tree-right-side-view",
        "count-good-nodes-in-binary-tree",
        "valid-binary-search-tree",
        "kth-smallest-integer-in-bst",
        "construct-binary-tree-from-preorder-and-inorder-traversal",
        "binary-tree-maximum-path-sum",
        "serialize-and-deserialize-binary-tree",
    ],
    "Tries": [
        "implement-trie",
        "design-word-search-data-structure",
        "search-for-word-ii",
    ],
    "Heap / Priority Queue": [
        "kth-largest-integer-in-a-stream",
        "last-stone-weight",
        "k-closest-points-to-origin",
        "kth-largest-element-in-an-array",
        "task-scheduling",
        "twitter-design",
        "find-median-in-a-data-stream",
    ],
    "Backtracking": [
        "subsets",
        "combination-target-sum",
        "permutations",
        "subsets-ii",
        "combination-sum-ii",
        "search-for-word",
        "palindrome-partitioning",
        "letter-combinations-of-a-phone-number",
        "n-queens",
    ],
    "Graphs": [
        "count-number-of-islands",
        "clone-graph",
        "max-area-of-island",
        "pacific-atlantic-water-flow",
        "surrounded-regions",
        "rotting-fruit",
        "islands-and-treasure",
        "course-schedule",
        "course-schedule-ii",
        "valid-tree",
        "count-connected-components",
        "redundant-connection",
        "word-ladder",
    ],
    "Advanced Graphs": [
        "reconstruct-flight-path",
        "min-cost-to-connect-points",
        "network-delay-time",
        "swim-in-rising-water",
        "foreign-dictionary",
        "cheapest-flight-path",
    ],
    "1-D Dynamic Programming": [
        "climbing-stairs",
        "min-cost-climbing-stairs",
        "house-robber",
        "house-robber-ii",
        "longest-palindrome-substring",
        "palindromic-substrings",
        "decode-ways",
        "coin-change",
        "maximum-product-subarray",
        "word-break",
        "longest-increasing-subsequence",
        "partition-equal-subset-sum",
    ],
    "2-D Dynamic Programming": [
        "count-paths",
        "longest-common-subsequence",
        "buy-and-sell-with-cooldown",
        "coin-change-ii",
        "target-sum",
        "interleaving-string",
        "longest-increasing-path-in-matrix",
        "count-subsequences",
        "edit-distance",
        "burst-balloons",
        "regular-expression-matching",
    ],
    "Greedy": [
        "maximum-subarray",
        "jump-game",
        "jump-game-ii",
        "gas-station",
        "hand-of-straights",
        "merge-triplets-to-form-target-triplet",
        "partition-labels",
        "valid-parenthesis-string",
    ],
    "Intervals": [
        "insert-new-interval",
        "merge-intervals",
        "non-overlapping-intervals",
        "meeting-schedule",
        "meeting-schedule-ii",
        "minimum-interval-to-include-each-query",
    ],
    "Math & Geometry": [
        "rotate-matrix",
        "spiral-matrix",
        "zero-matrix",
        "happy-number",
        "plus-one",
        "pow-x-n",
        "multiply-strings",
        "detect-squares",
    ],
    "Bit Manipulation": [
        "single-number",
        "number-of-one-bits",
        "counting-bits",
        "reverse-bits",
        "missing-number",
        "sum-of-two-integers",
        "reverse-integer",
    ],
}

BAR_WIDTH = 10
START = "<!-- NEETCODE_PROGRESS_START -->"
END = "<!-- NEETCODE_PROGRESS_END -->"


def progress_bar(solved: int, total: int) -> str:
    filled = round(solved / total * BAR_WIDTH) if total else 0
    return "▓" * filled + "░" * (BAR_WIDTH - filled)


def get_solved() -> set[str]:
    if not SOLUTIONS_DIR.exists():
        return set()
    return {p.name for p in SOLUTIONS_DIR.iterdir() if p.is_dir()}


def build_section(solved: set[str]) -> str:
    total_solved = sum(
        sum(1 for slug in slugs if slug in solved)
        for slugs in CATEGORIES.values()
    )
    total_problems = sum(len(s) for s in CATEGORIES.values())

    pct = int(total_solved / total_problems * 100) if total_problems else 0
    overall_bar = progress_bar(total_solved, total_problems)

    rows = [
        f"## NeetCode 150 — {total_solved} / {total_problems} solved ({pct}%)",
        "",
        f"`{overall_bar}` {pct}%",
        "",
        "| Category | Solved | Progress |",
        "|:---|:---:|:---|",
    ]

    for category, slugs in CATEGORIES.items():
        n = len(slugs)
        s = sum(1 for slug in slugs if slug in solved)
        bar = progress_bar(s, n)
        rows.append(f"| {category} | {s} / {n} | `{bar}` |")

    rows += [
        "",
        "*Updated automatically on every push via GitHub Actions.*",
    ]
    return "\n".join(rows)


def update_readme(section: str) -> None:
    text = README.read_text()
    block = f"{START}\n\n{section}\n\n{END}"
    pattern = re.compile(
        rf"{re.escape(START)}.*?{re.escape(END)}", re.DOTALL
    )
    if pattern.search(text):
        new_text = pattern.sub(block, text)
    else:
        new_text = text.rstrip() + f"\n\n{block}\n"
    README.write_text(new_text)


if __name__ == "__main__":
    solved = get_solved()
    section = build_section(solved)
    update_readme(section)
    total = sum(len(s) for s in CATEGORIES.values())
    matched = sum(
        sum(1 for slug in slugs if slug in solved)
        for slugs in CATEGORIES.values()
    )
    print(f"Done — {matched}/{total} NeetCode 150 problems solved.")
