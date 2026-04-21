# DustVision Workflow

## Communication Model
- **Caveman Protocol**: Ultra-terse, fluff-free technical communication for internal state updates.
- **Fragments Mandatory**: Drop articles, conjunctions, pleasantries.

## Directory Standards
- `data/`: Raw and processed datasets.
- `ml/`: Training pipelines, models, and evaluation outputs.
- `control/`: Logic engines, orchestrators, and APIs.
- `docs/`: Public documentation.
- `Archives/`: Internal roadmap, future steps, and historical notes.
- `conductor/`: Project context artifacts.

## Documentation Rules
- All `*.md` files except `README.md` must be saved to `Archives/` (or `conductor/` if context).
- `README.md` stays in root.

## Development Loop
1. **Goal Parse**: Determine target spec.
2. **Retrieve**: Find exact file/snippet using context tools.
3. **Plan**: Order steps and map dependencies.
4. **Act**: Implement following Tech Stack patterns.
5. **Verify**: Test, lint, and edge check.
6. **Log**: Update `tracks.md` and `task.md`.
