function initializeLiffOrDie(myLiffId) {
    if (!myLiffId) {
        document.getElementById("liffAppContent").classList.add('hidden');
        document.getElementById("liffIdErrorMessage").classList.remove('hidden');
    } else {
        initializeLiff(myLiffId);
    }
}

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
            // alert('error' + JSON.stringify(err))
            // document.getElementById("liffAppContent").classList.add('hidden');
            // document.getElementById("liffInitErrorMessage").classList.remove('hidden');
        });
}

function initializeApp() {
    // displayLiffData();
    // displayIsInClientInfo();
    registerButtonHandlers();

    // check if the user is logged in/out, and disable inappropriate button
    if (liff.isLoggedIn()) {
        document.getElementById('liffLoginButton').disabled = true;
        check_user()
        liff.getProfile().then(function(profile){
            document.getElementById('userid').value = profile.userId;
        })
    } else {
        document.getElementById('liffLogoutButton').disabled = true;
    }
}

function registerButtonHandlers(){
    // closeWindow call
    document.getElementById('closeWindowButton').addEventListener('click', function() {
        if (!liff.isInClient()) {
            sendAlertIfNotInClient();
        } else {
            liff.closeWindow();
        }
    });
}

function check_user(){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/add_user', true);
    
    //リクエストに従って正しいヘッダー情報を送信してください
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    
    xhr.onreadystatechange = function() { // 状態が変化すると関数が呼び出されます。
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            // リクエストの終了。ここの処理を実行します。
        }
    }
    xhr.send("foo=bar&lorem=ipsum");
    // xhr.send(new Int8Array());
    // xhr.send(document);    
}