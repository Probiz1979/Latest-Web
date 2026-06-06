const fs = require('fs');
const js = fs.readFileSync('translations.js', 'utf8');
eval(js);
console.log(typeof translations);
console.log(translations['ar']['Home']);
const originalStr = "\n   Home   \n";
const lookupStr = originalStr.replace(/\s+/g, ' ').trim();
console.log(originalStr.replace(lookupStr, translations['ar'][lookupStr]));
