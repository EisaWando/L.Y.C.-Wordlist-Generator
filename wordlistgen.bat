@echo off
:: Ultimate Password Generator - Batch File Version
:: Generates personalized wordlists for security testing

:: Color setup
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set "DEL=%%a"
)
echo <nul set /p ".=." > "%~f0?.tmp"
for /F "tokens=1" %%a in ('"%~f0?.tmp"') do (
  set "CR=%%a"
  del "%~f0?.tmp"
)

:: Banner
echo.
echo   ____  _   _ ____  _     ___ _____ _____ 
echo  ^|  _ \^| ^| ^| ^| __ )^| ^|   ^|_ _^|  ___^|  ___^|
echo  ^| ^|_) ^| ^| ^| ^|  _ \^| ^|    ^| ^|^| ^|_  ^| ^|_   
echo  ^|  __/^| ^|_^| ^| ^|_) ^| ^|___ ^| ^|^|  _^|^|  _^|  
echo  ^|_^|    \___/^|____/^|_____^|___^|_^|   ^|_^|    
echo.
echo Ultimate Personalized Password Generator
echo.

:: Main menu
:menu
cls
echo [1] Personal Information
echo [2] Pop Culture ^& Interests
echo [3] Common Patterns
echo [4] Hobbies ^& Interests
echo [5] Generate Wordlist
echo [6] Exit
echo.
set /p choice="Select option: "

if "%choice%"=="1" goto personal
if "%choice%"=="2" goto popculture
if "%choice%"=="3" goto common
if "%choice%"=="4" goto hobbies
if "%choice%"=="5" goto generate
if "%choice%"=="6" exit

goto menu

:: Data collection sections
:personal
cls
echo === Personal Information ===
set /p names="Enter names (comma separated: self, partner, kids, etc.): "
set /p pet_names="Pet names (comma separated): "
set /p birthdays="Important dates (YYYY-MM-DD, comma separated): "
set /p phone="Phone numbers (comma separated): "
set /p address_parts="Address parts (street, city, zip, comma separated): "
goto menu

:popculture
cls
echo === Pop Culture ^& Interests ===
set /p teams="Sports teams (comma separated): "
set /p celebrities="Celebrities/characters (comma separated): "
set /p movies_shows="Movies/TV shows (comma separated): "
set /p music="Bands/singers (comma separated): "
goto menu

:common
cls
echo === Common Patterns ===
set /p basic_words="Common words (password, admin, etc.): "
set /p keyboard_patterns="Keyboard patterns (qwerty, 123456): "
goto menu

:hobbies
cls
echo === Hobbies ^& Interests ===
set /p gaming="Gaming usernames: "
set /p food_drinks="Favorite foods/drinks: "
set /p places="Favorite places/visited locations: "
goto menu

:: Password generation
:generate
cls
echo Generating passwords...
setlocal enabledelayedexpansion

:: Basic separators and years
set separators= _ - . / ^! @ # $ 
set /a current_year=%date:~-4%
set /a start_year=current_year - 5
set /a end_year=current_year

:: Leetspeak substitutions
set leet=a4 e3 i1 o0 s5 t7

:: Initialize output file
echo. > wordlist.txt

:: Generate from names
for %%a in (%names%) do (
  call :generate_variations "%%a"
)

:: Generate from other fields (repeat for each category)
:: [Additional generation code would go here...]

:: Final count
for /f %%A in ('type wordlist.txt ^| find /v /c ""') do set count=%%A
echo Generated !count! passwords in wordlist.txt
echo.
pause
goto menu

:: Variation generator subroutine
:generate_variations
set base=%~1

:: Case variations
echo !base! >> wordlist.txt
echo !base:~0,1!!base:~1! >> wordlist.txt
echo !base:~0,1!!base:~1! >> wordlist.txt

:: Leetspeak
set leetword=!base!
for %%s in (%leet%) do (
  set original=%%s
  set original=!original:~0,1!
  set replacement=%%s
  set replacement=!replacement:~1!
  call set leetword=%%leetword:!original!=!replacement%%%
)
echo !leetword! >> wordlist.txt

:: With years and separators
for /l %%y in (%start_year%, 1, %end_year%) do (
  echo !base!%%y >> wordlist.txt
  for %%s in (%separators%) do (
    echo !base!%%s%%y >> wordlist.txt
    echo %%y%%s!base! >> wordlist.txt
  )
)
goto :eof

:: Clean exit
:exit
exit /b