# Projekt "Enterprise AI Agent" – kompleksowy agent AI klasy enterprise do zastosowań bankowych.

## Opis
Agent wykorzystuje FastAPI, RAG pipeline, modele językowe i embeddingowe, a także integrację z zewnętrznymi usługami (np. Azure OpenAI).

## Struktura projektu
- `app/` – kod aplikacji
- `data/` – dokumenty i dane testowe
- `tests/` – testy jednostkowe, integracyjne i e2e
- `infrastructure/` – Docker, Terraform, skrypty CI/CD
- `frontend/` – aplikacja Streamlit
- `docs/` – dokumentacja i ADR

## Instalacja (lokalnie)
```bash
git clone git@github.com:mateuszgrzyb-pl/enterprise-ai-agent.git
cd enterprise_ai_agent
make dev-start
```
