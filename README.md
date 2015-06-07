# Custom Elements Importer
"Custom Elements Importer" is plugin for Sublime Text 2. When called via Command Palette, find all custom elements in file and adds "link" tag import at the cursor's position.

### Usage:
Run "Custom Elements Importer" using Command Palette (`Ctrl+Shift+P`) with "Import Custom Elements".

### Features:
- discovering html custom elements (based on the requirement that custom elements have at least one hyphen(-) in it's name)
- creating "link" tag imports of not yet imported tags definitions
- rich customizability via setting, such as:
  - default path for custom elements
  - defining elements' path based on name's prefix (ex. prefix "x" for elements "x-foo", "x-bar")
  - defining path per-tag (not based on prefix)
  - defining import dependencies (ex. "cool-icon" requires "cool-icons-set" to work properly)

### Settings:
Below is example settings file with descriptions of all properties
```javascript
{
	// default path if tags does not match neither "prefix_paths" not "tag_paths"
	"default_path": "bower_components",

	// define common paths for all elements with certain prefix
	"prefix_paths": {
		// example: "x": "my_tags/x"
	},

	// define paths per-tag
	"tag_paths": {
		// example: "x-tag": "my_tags/x-tag.html"
	},

	// define import dependencies if element requires additional files
	"tag_dependencies": {
		// example: "cool-icon": ["cool-icons-set"] 
	}
}
```