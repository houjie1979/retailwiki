@echo off
REM Build Sphinx documentation
echo Building documentation...
sphinx-build -b html source build\html

REM Check if build succeeded
if errorlevel 1 (
    echo Build failed. Exiting...
    exit /b 1
)

REM Enter build/html directory
echo Entering build/html directory...
cd build\html

REM Create .nojekyll file to disable Jekyll processing
echo Creating .nojekyll file...
echo. > .nojekyll

REM Initialize Git repository (if not already initialized)
echo Initializing Git repository...
if not exist .git (
    git init
    git checkout -b gh-pages
)

REM Add all files and commit
echo Adding files and committing...
git add .
git commit -m "Deploy documentation to gh-pages"

REM Push to remote gh-pages branch
echo Pushing to gh-pages branch...
git push -f git@github.ibm.com:jiehou/retailwiki.git gh-pages:gh-pages
git push -f git@github.com:houjie1979/retailwiki.git gh-pages:gh-pages

REM Return to project root directory
echo Returning to project root...
cd ..\..

echo Deployment completed successfully.