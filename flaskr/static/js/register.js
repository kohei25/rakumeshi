window.onload = function() {
    const defaultLiffId = "1656378583-rLZqp0ma";   // change the default LIFF value if you are not using a node server

    // DO NOT CHANGE THIS
    let myLiffId = "";

    myLiffId = defaultLiffId;
    initializeLiffOrDie(myLiffId);
};

/**
* Check if myLiffId is null. If null do not initiate liff.
* @param {string} myLiffId The LIFF ID of the selected element
*/
function initializeLiffOrDie(myLiffId) {
    if (!myLiffId) {
        document.getElementById("liffAppContent").classList.add('hidden');
        document.getElementById("liffIdErrorMessage").classList.remove('hidden');
    } else {
        initializeLiff(myLiffId);
    }
}

/**
* Initialize LIFF
* @param {string} myLiffId The LIFF ID of the selected element
*/
function initializeLiff(myLiffId) {
    liff
        .init({
            liffId: myLiffId
        })
        .then(() => {
            // start to use LIFF's api
            initializeApp();
        })
        .catch((err) => {
            document.getElementById("liffAppContent").classList.add('hidden');
            document.getElementById("liffInitErrorMessage").classList.remove('hidden');
        });
}

/**
 * Initialize the app by calling functions handling individual app components
 */
function initializeApp() {

    // check if the user is logged in/out, and disable inappropriate button
    if (liff.isLoggedIn()) {
        document.getElementById('liffLoginButton').disabled = true;
        liff.getProfile().then(function(profile) {
            var lineId = profile.userId;
            document.getElementById('userid').value = lineId;
            check_user(lineId);
        }).catch(function(error) {
            window.alert('Error getting profile: ' + error);
        });
    } else {
        document.getElementById('liffLogoutButton').disabled = true;
    }
}

function check_user(lineId){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/add_user', true);
    
    //リクエストに従って正しいヘッダー情報を送信してください
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    
    xhr.onreadystatechange = function() { // 状態が変化すると関数が呼び出されます。
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            // リクエストの終了。ここの処理を実行します。
        }
    }
    xhr.send(`lineid=${lineId}`);
}
