import React, {useState} from 'react'
import liff from '@line/liff'
import {IProfile} from './type'

export const initializeLiffOrDie = (myLiffId: string) => {
    if(!myLiffId){
        // setButton(prevstate => ({
        //     ...prevstate,
        //     content: false,
        //     liffIdErrorMessage: true
        // }))
    } else {
        liff
        .init({
            liffId: myLiffId
        })
        .then(() => {
            if (liff.isLoggedIn()){
                // setButton(prevstate => ({
                //     ...prevstate,
                //     login: false
                // }))
            } else {
                // setButton(prevstate => ({
                //     ...prevstate,
                //     logout: false
                // }))
            }
        })
        .catch((err: any) => {
            // setButton(prevstate => ({
            //     ...prevstate,
            //     content: false,
            //     liffInitErrorMessage: true
            // }))
            console.log(err)
        })
    }
}

export const closeWindow = () => {
    liff.closeWindow()
}

export const openWindow = () => {
    liff.openWindow({
        url: 'https://sakurazaka46.com/s/s46/',
        external: true
    });
}

export const sendMessage = () => {
    if (!liff.isInClient()) {
        sendAlertIfNotInClient();
    } else {
        liff.sendMessages([{
            'type': 'text',
            'text': "You've successfully sent a message! Hooray!"
    }]).then(function() {
        window.alert('Message sent')
    }).catch(function(error: any) {
        window.alert('Error sending message: ' + error);
    });
}
}

const getAccessToken = () => {
    if (!liff.isLoggedIn() && !liff.isInClient()) {
        alert('To get an access token, you need to be logged in. Please tap the "login" button below and try again.');
    } else {
        // setAccessToken(liff.getAccessToken())
        // toggleElement('accessToken', isOpen.accessToken)
    }
}



export function getProfile(){
    liff.getProfile().then(function(profile: any) {
        const setProfile: IProfile = {
            userId: profile.userId,
            displayName: profile.displayName,
            pictureUrl: profile.pictureUrl, 
            statusMessage: profile.statusMessage
        }
        return {flag: 0, profile: setProfile}
    }).catch(function(error: any) {
        window.alert('Error getting profile: ' + error);
        return {flag: 1, profile: undefined}
    });
}


function sendAlertIfNotInClient() {
    alert('This button is unavailable as LIFF is currently being opened in an external browser.');
}



//   function shareTargetPicker(){
//     if (liff.isApiAvailable('shareTargetPicker')) {
//         liff.shareTargetPicker([{
//             'type': 'text',
//             'text': 'Hello, World!'
//         }]).then(
//             document.getElementById('shareTargetPickerMessage').textContent = "Share target picker was launched."
//         ).catch(function (res) {
//             document.getElementById('shareTargetPickerMessage').textContent = "Failed to launch share target picker.";
//         });
//     } else {
//         document.getElementById('shareTargetPickerMessage').innerHTML = "<div>Share target picker unavailable.<div><div>This is possibly because you haven't enabled the share target picker on <a href='https://developers.line.biz/console/'>LINE Developers Console</a>.</div>";
//     }
//   }