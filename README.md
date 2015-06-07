# Custom Elements Importer
"Custom Elements Importer" is plugin for Sublime Text 2. When called via Command Palette, find all custom elements in file and adds "link" tag import at the cursor's position.

### Usage:
Run "Custom Elements Importer" using Command Palette (`Ctrl+Shift+P`) with "Import Custom Elements".

### Features:
- discovering html custom elements
- creating "link" tag imports of not yet imported tags definitions
- easy to customize via settings, such as:
  - default path for custom elements
  - defining elements' path based on name's prefix (ex. prefix "x" for elements "x-foo", "x-bar")
  - defining path per-tag (not based on prefix)
  - defining import dependencies (ex. "cool-icon" requires "cool-icons-set" to work properly)

### Settings:
Below is example settings file with descriptions of all properties.
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

### License
```
The MIT License (MIT)

Copyright (c) 2015 JMendyk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
