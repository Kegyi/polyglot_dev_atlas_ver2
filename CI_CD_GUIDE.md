# CI/CD Integration Guide

This document describes the Continuous Integration and Continuous Deployment setup for the Polyglot Dev Atlas.

## GitHub Actions Workflows

The Atlas includes three main GitHub Actions workflows:

### 1. **Build & Validate Atlas** (`build.yml`)
- **Triggers:** Push to main/master/develop, Pull Requests
- **Python versions tested:** 3.10, 3.11
- **Steps:**
  - Checkout code
  - Set up Python environment
  - Build Atlas with strict validation
  - Validate external links (dead link checker)
  - Check build artifacts
  - Deploy to GitHub Pages (on main push only)

**Features:**
- Strict schema validation prevents broken JSON from merging
- Dead link checker validates all external URLs
- Artifacts uploaded for 30 days (audit trail)
- Automatic deployment to GitHub Pages on successful main branch push

### 2. **Dead Link Check** (`dead-links.yml`)
- **Triggers:** Daily at 2 AM UTC, Manual dispatch (workflow_dispatch), Content changes
- **Purpose:** Validates all external URLs in content
- **Options:**
  - Runs with 15-second timeout per URL
  - Creates GitHub issue if broken links found
  - Can be manually triggered via GitHub Actions UI

**Usage:**
```bash
# Manually trigger from GitHub Actions tab or CLI
gh workflow run dead-links.yml
```

### 3. **Validate Pull Request** (`validate-pr.yml`)
- **Triggers:** Pull requests to main/master/develop
- **Purpose:** Quick validation before merge
- **Checks:**
  - JSON schema validation
  - Content discovery
  - Internal link verification
  - Comments results on PR

## Local Development Workflow

### Pre-commit Validation
```bash
# Validate content without building
python build_system/core.py --validate-only

# Check for schema errors in strict mode
python build_system/core.py --strict-validation

# Validate external links
python build_system/dead_link_checker.py --verbose
```

### Build with Watch Mode
```bash
# Automatic rebuild on file changes
python build_system/core.py --watch
```

### Full Build
```bash
# Standard build
python build_system/core.py

# Build and validate
python build_system/core.py --strict-validation
```

## Environment Variables

Set these in your GitHub repository settings under `Settings > Secrets and variables > Actions`:

- `PYTHON_VERSION`: Override Python version (default: 3.11)
- `PYTHONIOENCODING`: Set to `utf-8` (should be automatic)

## Deployment

### Automatic Deployment (Main Branch)
- Build completes successfully on `main` push
- Artifacts automatically deployed to GitHub Pages
- Available at: `https://[username].github.io/polyglot_dev_atlas_ver2/`

### Manual Deployment
```bash
# Build locally
cd polyglot_dev_atlas_ver2
python build_system/core.py

# Deploy to GitHub Pages manually
gh repo deploy --dir dist
```

## Exit Codes

The build system uses standard exit codes:

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Validation error (strict mode) or broken links (dead link checker) |

## Troubleshooting

### Build Fails: "Module not found"
**Solution:** Ensure Python 3.10+ is installed
```bash
python --version  # Should be 3.10+
```

### Dead Link Checker Timeout
**Solution:** Increase timeout in workflow
```yaml
python build_system/dead_link_checker.py --timeout 20
```

### GitHub Pages Not Updating
**Solution:** Check deployment settings
1. Go to `Settings > Pages`
2. Ensure "Source" is set to "GitHub Actions"
3. Check workflow run status in `Actions` tab

## Best Practices

### Before Merging to Main

1. **Run local validation:**
   ```bash
   python build_system/core.py --strict-validation
   ```

2. **Check external links:**
   ```bash
   python build_system/dead_link_checker.py --strict
   ```

3. **Test in watch mode:**
   ```bash
   python build_system/core.py --watch
   ```

### PR Guidelines

- Ensure all checks pass before requesting review
- Add descriptive commit messages
- Reference related issues (`Fixes #123`)
- Include updated content files only

### Content Updates

- Keep JSON valid (test locally before pushing)
- Validate new external links
- Update search metadata if adding pages
- Test with multiple Python versions locally if possible

## Advanced Configuration

### Custom Domain
Update GitHub Pages settings to use custom domain:
1. `Settings > Pages > Custom domain`
2. Add DNS records as instructed

### Caching
The workflows use GitHub's cache for Python dependencies:
- Cache key: `pip-${{ hashFiles('**/requirements.txt') }}`
- Automatically managed by actions/setup-python@v4

### Matrix Testing
Add more Python versions in `build.yml`:
```yaml
matrix:
  python-version: ['3.10', '3.11', '3.12']
```

## References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Pages Deployment Action](https://github.com/actions/deploy-pages)
- [Python Setup Action](https://github.com/actions/setup-python)
