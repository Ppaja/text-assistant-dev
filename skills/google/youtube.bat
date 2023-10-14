@echo off
set /p suchbegriff="Enter a search term for YouTube: "
start "" "https://www.youtube.com/results?search_query=%suchbegriff%"
