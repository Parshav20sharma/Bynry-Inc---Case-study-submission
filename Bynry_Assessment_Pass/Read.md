# **Part 3: Quick Start Guide**

## **What it Tests**
API → Web UI → Mobile → Security → Cleanup  
Desktop Chrome + iPhone viewport  
company1 vs company2 tenant isolation

## **Requirements (2 minutes)**
```bash
pip install -r requirements.txt
playwright install chromium
```

**If missing:**
```
python -m pip install pytest playwright
npx playwright install chromium
```

## **Run Test**
**VS Code Terminal (Ctrl+`):**
```bash
pytest tests/ -v -s
```

## **Expected Output**
```
collected 1 item
tests/test_integration/test_project_creation_flow.py::test_project_creation_flow PASSED [100%]
1 passed in 4s
```

**Visual:** 2 Chrome windows open (Desktop + Mobile)

## **Fix Issues**
```
Hang → Ctrl+C → playwright install chromium
No tests → Check pytest.ini exists
Import error → pip install -r requirements.txt
