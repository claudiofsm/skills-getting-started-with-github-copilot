# Backend API Tests

This directory contains backend tests for the FastAPI app in `src/app.py`.

## Scope

These tests cover:
- Listing activities (`GET /activities`)
- Registering a participant (`POST /activities/{activity_name}/signup`)
- Unregistering a participant (`DELETE /activities/{activity_name}/participants`)

## Test structure

- `conftest.py`: shared pytest fixtures
- `test_activities.py`: read/list endpoint behavior
- `test_signup.py`: signup success and error paths
- `test_unregister.py`: unregister success and error paths

## Fixtures and state isolation

The app stores activity data in an in-memory dictionary. To keep tests deterministic and independent:
- `conftest.py` snapshots the original `activities` data
- an `autouse` fixture resets the in-memory state before each test
- each test runs against a clean baseline

## Running tests

From the repository root:

```bash
python3 -m pytest tests -v
```
