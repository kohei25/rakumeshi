const endpoint = 'https://15f6-240d-1a-d6-a600-9893-9fb8-f052-2825.ngrok.io/liff'

/**
* Initialize LIFF
* @param {string} myLiffId The LIFF app ID of the selected element
*/
function initializeLiff(myLiffId){
    liff
        .init({
            liffid: myLiffId
        })
        .then(() => {
            initializeApp()
        })
        .catch((err) => {
            document.getElementById('liffAppContent').classList.add('hidden')
            document.getElementById('liffInitErrorMessage').classList.remove('hidden')
        })
}

/**
* Display data generated by invoking LIFF methods
*/
function displayLiffData() {
    document.getElementById('browserLanguage').textContent = liff.getLanguage();
    document.getElementById('sdkVersion').textContent = liff.getVersion();
    document.getElementById('isInClient').textContent = liff.isInClient();
    document.getElementById('isLoggedIn').textContent = liff.isLoggedIn();
    document.getElementById('deviceOS').textContent = liff.getOS();
    document.getElementById('lineVersion').textContent = liff.getLineVersion();
}

// login call, only when external browser or LINE's in-app browser is used
document.getElementById('liffLoginButton').addEventListener('click', function() {
    if (!liff.isLoggedIn()) {
        liff.login();
    }
});

// logout call only when external browse
document.getElementById('liffLogoutButton').addEventListener('click', function() {
    if (liff.isLoggedIn()) {
        liff.logout();
        window.location.reload();
    }
});

if (!liff.isLoggedIn()) {
    liff.login({ redirectUri: endpoint });
    //ドメイン名とパス（https://example.com/path）がエンドポイントURLと一致しているか検証します。
}