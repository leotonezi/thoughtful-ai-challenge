# 🤖 Robotic Package Sorter

This project implements a function for Thoughtful’s robotic arm to classify packages based on their **volume** and **mass**.

---

## 📦 Classification Logic

- A package is **bulky** if:
  - Volume (Width × Height × Length) ≥ 1,000,000 cm³, or
  - Any single dimension ≥ 150 cm
- A package is **heavy** if:
  - Mass ≥ 20 kg

### ➕ Decision Matrix:

| Bulky | Heavy | Result     |
|-------|--------|------------|
| ❌    | ❌     | STANDARD   |
| ✅    | ❌     | SPECIAL    |
| ❌    | ✅     | SPECIAL    |
| ✅    | ✅     | REJECTED   |

---

## 🚀 Usage

```python
from sort import sort

result = sort(100, 100, 100, 10)
print(result)  # Output: SPECIAL
```


📂 Files
	•	sort.py: main function
	•	test_sort.py: test suite using pytest
	•	README.md: this documentation
	•	requirements.txt: project dependencies

⸻

## 🧪 Testing

This project uses pytest for unit testing.

✅ Step 1: Install dependencies

pip install -r requirements.txt

Or install pytest directly:

pip install pytest

▶️ Step 2: Run the tests

pytest

This will run all tests defined in test_sort.py, including:
	•	✅ Standard packages
	•	✅ Bulky (volume or dimension)
	•	✅ Heavy
	•	✅ Rejected (both)
	•	✅ Type error cases (e.g. strings or None values)


## 🛠️ Next Steps (WIP)

If you'd like to continue improving this project, here are some ideas:

•⁠  ⁠[ ] *Input validation*: Add checks to reject negative or non-numeric inputs
•⁠  ⁠[ ] *Structured return*: Instead of just returning a string, return a dictionary with detailed classification info (e.g. ⁠ { classification: "SPECIAL", bulky: True, heavy: False } ⁠)
•⁠  ⁠[ ] *Batch processing*: Add support for classifying multiple packages at once
•⁠  ⁠[ ] *Logging*: Log which rule triggered each classification for better traceability
•⁠  ⁠[ ] *API wrapper*: Create a simple FastAPI endpoint to expose the ⁠ sort() ⁠ function as a service
•⁠  ⁠[ ] *More test cases*: Add edge case and stress tests (e.g. extremely large or malformed input)