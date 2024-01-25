## Setting up your directories
assume directory layout is set up like this
```
projectRoot
├── src
│   ├── file1.js
│   └── file2.js
├── built
└── tsconfig.json
```
use JS file as inputs to TS, 
seprate input directory and output directory to prevent TS from overwriting them.

## Writing a Configuration File
tsconfig.json 
```
{
  "compilerOptions": {
    "outDir": "./built",
    "allowJs": true,
    "target": "es5"
  },
  "include": ["./src/**/*"]
}
```
Here we’re specifying a few things to TypeScript:

Read in any files it understands in the src directory (with include).
Accept JavaScript files as inputs (with allowJs).
Emit all of the output files in built (with outDir).
Translate newer JavaScript constructs down to an older version like ECMAScript 5 (using target).
