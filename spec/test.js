const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', function (input) {
    console.log(decrypt(input));
    rl.close();
});

rl.on('close', function() {
    process.exit(0);
});

function decrypt(encryptText)

{
    const result = [];
    const keyMap = {
        "2":'abc',
        "3":'def',
        "4":'ghi',
        "5":'jkl',
        "6":'mno',
        "7":'pqrs',
        "8":'tuv',
        "9":'wxyz',
    }
    const charMap = {};
    Object.keys(keyMap).forEach((key)=>{
        keyMap[key].split('').forEach(c=>{
            charMap[c] = key;
        })
    })
    for(let i=0;i<encryptText.length;i++){
        const cur = encryptText[i];
        if(/[a-z]/.test(cur)){
            result.push(charMap[cur]);
        }else if(/[A-Z]/.test(cur)){
            if(cur ===  'Z'){
                result.push('a');
            }else {
                result.push(String.fromCodePoint(cur.charCodeAt()+33));
            }
        }else{
            result.push(cur);
        }
    }
    return result.join('');
}

