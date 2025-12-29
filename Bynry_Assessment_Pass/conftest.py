import pytest
from playwright.sync_api import sync_playwright

class FakeResponse:
    def __init__(self, status_code, json_data=None):
        self.status_code = status_code
        self._json = json_data or {}

    def json(self):
        return self._json

class MockAPIClient:
    def __init__(self):
        self.token = "mock-token-123"
        self.created_projects = []

    def post(self, endpoint, headers=None, json=None):
        print(f"🎯 MOCK API: POST {endpoint}")
        project_id = f"proj_{len(self.created_projects) + 1}"
        self.created_projects.append(project_id)
        return FakeResponse(
            201,
            {"id": project_id, "name": json.get("name"), "status": "active"}
        )

    def delete(self, endpoint, headers=None):
        print(f"🗑️ MOCK API: DELETE {endpoint}")
        return FakeResponse(204)

@pytest.fixture(scope="session")
def api_client():
    return MockAPIClient()

@pytest.fixture(scope="session")
def playwright_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(playwright_browser):
    context = playwright_browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def mobile_page(playwright_browser):
    context = playwright_browser.new_context(
        viewport={"width": 375, "height": 812},
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)"
    )
    page = context.new_page()
    yield page
    context.close()