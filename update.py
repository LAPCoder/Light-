# Script to generate "icons/Light#-icon-theme.json"
# All icons are in the folder "icons/svg"
# The script will generate a json file with the following format:
# {
#		"iconDefinitions": {
#			"html": {
#				"iconPath": "./svg/html.svg",
#			},
#			"css": {
#				"iconPath": "./svg/css.svg",
#			},
#			"js": {
#				"iconPath": "./svg/js.svg",
#			},
#			"php": {
#				"iconPath": "./svg/php.svg",
#			},
#			...
#			"folder-html": {
#				"iconPath": "./svg/folder-html.svg",
#			},
#			"folder-html-open": {
#				"iconPath": "./svg/folder-html-open.svg",
#			},
#			"folder-css": {
#				"iconPath": "./svg/folder-css.svg",
#			},
#			"folder-css-open": {
#				"iconPath": "./svg/folder-css-open.svg",
#			},
#			...
#		},
#		"folderNames": {
#			"html": "folder-html",
#			"css": "folder-css",
#			"js": "folder-js",
#			...
#		},
#		"folderNamesExpanded": {
#			"html": "folder-html-open",
#			"css": "folder-css-open",
#			"js": "folder-js-open",
#			...
#		},
#		"fileExtensions": {
#			"html": "html",
#			"css": "css",
#			"js": "js",
#			...
#		},
#		"fileNames": {
#			"index.html": "html",
#			"styles.css": "css",
#			".gitattribites": "git",
#			...
#		},
#		"languageIds": {
#			"html": "html",
#			"css": "css",
#			"js": "javascript",
#			...
#		},
#		"file": "file",
#		"hidesExplorerArrows": false,
#		"folder": "folder",
#		"folderExpanded": "folder-open",
#		"rootFolder": "folder-root",
#		"rootFolderExpanded": "folder-root-open"
#	}

# Import modules
import json
import os

# Define variables

fileExtensions = [
	["html", "html"],
	["css", "css"],
	["js", "javascript"],
	["php", "php"],
	["py", "python"],
	["rb", "ruby"],
	["sh", "shell"],
	["xml", "xml"],
	["yml", "yaml"],
	["yaml", "yaml"],
	["json", "json"],
	["md", "markdown"],
	["markdown", "markdown"],
	["mark", "markdown"],
	["txt", "text"],
	["ini", "ini"],
	["git", "git"],
	["gitattributes", "git"],
	["gitignore", "git"],
	["gitmodules", "git"],
	["gitkeep", "git"],
	
]

fileName = [
	["index.html", "html"],
	["styles.css", "css"],
	[".gitattributes", "git"],
	[".gitignore", "git"],
	[".gitmodules", "git"],
	[".gitkeep", "git"],
	["readme.md", "readme"],
	["readme.markdown", "readme"],
	["readme.txt", "readme"],
	["readme.rst", "readme"],
	["readme", "readme"],
	["license", "license"],
	["license.md", "license"],
	["license.txt", "license"],
	["license.markdown", "license"],

]

fileId = [
	["4u", "4u"],
	["alex", "alex"],
	["arduino", "arduino"],
	["atom", "atom"],
	["babel", "babel"],
	["babel-node", "babel"],
	["babel-eslint", "babel"],
	["babel-jest", "babel"],
	["babel-preset-env", "babel"],
	["bash", "bash"],
	["bower", "bower"],
	["bibtex", "bibtex"],
	["bicep", "bicep"],
	["c", "c"],
	["cpp", "cpp"],
	["csharp", "csharp"],
	["css", "css"],
	["docker", "docker"],
	["docker-compose", "docker"],
	["docker-machine", "docker"],
	["docker-stack", "docker"],
	["dockerfile", "docker"],

]


# Path to the svg folder
svg_path = "icons/svg"
# Path to the json file
json_path = "icons/Light#-icon-theme.json"
# Files
files = os.listdir(svg_path)

# Create json file
json_file = open(json_path, "w")
# Erase the file
json_file.truncate()
# Write the json file
json_file.write("{")
json_file.write("\n\t\"iconDefinitions\": {")
for file in files:
	json_file.write("\n\t\t\"" + file.split(".")[0] + "\": {")
	json_file.write("\n\t\t\t\"iconPath\": \"./svg/" + file + "\"")
	json_file.write("\n\t\t},")
json_file.write("\n\t},")
json_file.write("\n\t\"folderNames\": {")
for file in files:
	if file.split(".")[0].split("-")[0] == "folder" and len(file.split(".")[0].split("-")) == 2:
		json_file.write("\n\t\t\"" + file.split(".")[0].split("-")[1] + "\": \"" + file.split(".")[0] + "\",")
json_file.write("\n\t},")
json_file.write("\n\t\"folderNamesExpanded\": {")
for file in files:
	if file.split(".")[0].split("-")[0] == "folder" and len(file.split(".")[0].split("-")) == 3:
		json_file.write("\n\t\t\"" + file.split(".")[0].split("-")[1] + "\": \"" + file.split(".")[0] + "\",")
json_file.write("\n\t},")
json_file.write("\n\t\"fileExtensions\": {")
for line in fileExtensions:
	json_file.write("\n\t\t\"" + line[0] + "\": \"" + line[1] + "\",")
json_file.write("\n\t},")
json_file.write("\n\t\"fileNames\": {")
for file in fileName:
	json_file.write("\n\t\t\"" + file[0] + "\": \"" + file[1] + "\",")
json_file.write("\n\t},")
json_file.write("\n\t\"languageIds\": {")
for line in fileId:
	json_file.write("\n\t\t\"" + line[1] + "\": \"" + line[0] + "\",")
json_file.write("\n\t},")
json_file.write("\n\t\"file\": \"file\",")
json_file.write("\n\t\"hidesExplorerArrows\": false,")
json_file.write("\n\t\"folder\": \"folder\",")
json_file.write("\n\t\"folderExpanded\": \"folder-open\",")
json_file.write("\n\t\"rootFolder\": \"folder-root\",")
json_file.write("\n\t\"rootFolderExpanded\": \"folder-root-open\"")
json_file.write("\n}")
json_file.close()
print("Done!")
