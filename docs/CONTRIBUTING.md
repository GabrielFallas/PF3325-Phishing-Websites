# Contributing to Phishing Detection PF3325

Thank you for your interest in contributing to this project! This is an academic project for the PF3325 course.

## Project Guidelines

### Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and modular

Example:

```python
def preprocess_features(X: pd.DataFrame) -> np.ndarray:
    """
    Preprocess feature matrix by applying standard scaling.

    Args:
        X: Feature matrix with shape (n_samples, n_features)

    Returns:
        Scaled feature matrix as NumPy array
    """
    scaler = StandardScaler()
    return scaler.fit_transform(X)
```

### Commit Messages

Use clear, descriptive commit messages following this format:

```
<type>: <subject>

<body>
```

Types:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Examples:

```
feat: add real-time feature extraction from URLs

Implemented the 30 feature extractors based on Mohammad et al. (2012)
rules for analyzing URLs in real-time.

---

docs: update README with API usage examples

Added code snippets showing how to use the FastAPI endpoints
for phishing detection.
```

### Git Workflow

1. **Create a feature branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes and commit:**

   ```bash
   git add .
   git commit -m "feat: your descriptive message"
   ```

3. **Push to your branch:**

   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request** (if working in a team)

### Branch Naming

- `feature/` - New features (e.g., `feature/api-endpoint`)
- `fix/` - Bug fixes (e.g., `fix/preprocessing-error`)
- `docs/` - Documentation updates (e.g., `docs/api-guide`)
- `experiment/` - Experimental work (e.g., `experiment/new-architecture`)

### Testing

Before committing:

1. Test your code locally
2. Ensure all notebooks run without errors
3. Verify that the API starts successfully
4. Check that models train without issues

### Documentation

- Update README.md if adding new features
- Add docstrings to new functions
- Update relevant section READMEs
- Include code examples where appropriate

### Dependencies

When adding new dependencies:

1. Add to `requirements.txt`
2. Document why the dependency is needed
3. Specify minimum version if critical

### Project Structure

Maintain the existing project structure:

- Source code → `src/`
- Notebooks → `notebooks/`
- Data → `data/`
- Models → `models/` (not tracked)
- Reports → `reports/`
- Presentations → `presentations/`

## Questions?

For questions or clarifications, please:

1. Check the `PLAN_PROYECTO.md` for project details
2. Review existing documentation
3. Open an issue for discussion
4. Contact team members

## Academic Integrity

This is an academic project for PF3325. Please:

- Respect your institution's academic integrity policies
- Cite all external sources and references
- Document any code adapted from external sources
- Be transparent about collaboration

---

Thank you for contributing to this project! 🚀

