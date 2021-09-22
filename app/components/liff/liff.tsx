import type { NextPage } from 'next'
import { useEffect, useState } from 'react'
import Head from 'next/head'
import Image from 'next/image'
// import styles from '../styles/Liff.module.css'
import styles from '../../styles/Liff.module.css'
import octcat from '../public/octcat.jpg'
import liff from '@line/liff'
import {closeWindow, openWindow, sendMessage} from './init'
import { TDictLiffProfile, TLiffProfile } from './type'

export default function Liff(){
    const [isOpen, setIsOpen] = useState({
        accessToken: false,
        profile: false,
    })
    const [button, setButton] = useState({ 
        login: true,
        logout: true,
        content: true,
        liffIdErrorMessage: false,
        liffInitErrorMessage: false
    })
    const [accessToken, setAccessToken] = useState<string | null>(null)
    const [profile, setProfile] = useState<TLiffProfile | undefined>(undefined)

    const initializeLiffOrDie = (myLiffId: string) => {
        if(!myLiffId){
        } else {
            liff
            .init({
                liffId: myLiffId
            })
            .then(() => {
                if (liff.isLoggedIn()){
                } else {
                }
            })
            .catch((err: any) => {
                console.log(err)
            })
        }
    }

    useEffect(() => {
        const myLiffId = '1656441685-0MEzq1zq'
        initializeLiffOrDie(myLiffId)
    }, [])

    const getAccessToken = () => {
        if (!liff.isLoggedIn() && !liff.isInClient()) {
            alert('To get an access token, you need to be logged in. Please tap the "login" button below and try again.');
        } else {
            setAccessToken(liff.getAccessToken())
            toggleElement('accessToken', isOpen.accessToken)
        }
    }

    function getProfile(): [number, TDictLiffProfile]{
        const responce: TDictLiffProfile = {}
        liff.getProfile().then(function(profile: any) {
            const responce: TDictLiffProfile = {}
            responce[0] = {
                userId: profile.userId,
                displayName: profile.displayName,
                pictureUrl: profile.pictureUrl, 
                statusMessage: profile.statusMessage
            }
            setProfile(responce[0])
            toggleElement('profile', isOpen.profile)
            return [0, responce]
        }).catch(function(error: any) {
            window.alert('Error getting profile: ' + error);
            return [1, responce]
        });
        return [2, responce]
    }

    function toggleElement(name: string, value: boolean){
        setIsOpen(prevState => ({
            ...prevState,
            [name]: !value
        }))
    }

  return (
    <body className={styles.html}>
        <div id="liffAppContent" className={button.content? '':styles.hidden}>
            {/* <!-- ACTION BUTTONS --> */}
            <div className={styles.buttonGroup}>
                <div className={styles.buttonRow}>
                    <button id="openWindowButton" onClick={openWindow}>Open External Window</button>
                    <button id="closeWindowButton" onClick={closeWindow}>Close LIFF App</button>
                </div>
                <div className={styles.buttonRow}>
                    <button id="sendMessageButton" onClick={sendMessage}>Send Message</button>
                    <button id="getAccessToken" onClick={getAccessToken}>Get Access Token</button>
                </div>
                <div className={styles.buttonRow}>
                    <button id="getProfileButton" onClick={getProfile}>Get Profile</button>
                    <button id="shareTargetPicker">Open Share Target Picker</button>
                </div>
            </div>
            <div id="shareTargetPickerMessage"></div>
            {/* <!-- ACCESS TOKEN DATA --> */}
            <div id="accessTokenData" className={`styles.textLeft ${isOpen.accessToken? '':styles.hidden}`}>
                <h2>Access Token</h2>
                <a href="#" onClick={() => toggleElement('accessToken', isOpen.accessToken)}>Close Access Token</a>
                <table>
                    <tr>
                        <th>accessToken</th>
                        <td id="accessTokenField">{accessToken}</td>
                    </tr>
                </table>
            </div>
            {/* <!-- PROFILE INFO --> */}
            <div id="profileInfo" className={`styles.textLeft ${isOpen.profile? '':styles.hidden}`}>
                <h2>Profile</h2>
                <a onClick={() => toggleElement('profile', isOpen.profile)}>Close Profile</a>
                <div id="profilePictureDiv">
                    {/* <Image src={profile?.pictureUrl? profile.pictureUrl:''} alt='profile Picture' /> */}
                </div>
                <table>
                    <tr>
                        <th>userId</th>
                        <td id="userIdProfileField">{profile?.userId}</td>
                    </tr>
                    <tr>
                        <th>displayName</th>
                        <td id="displayNameField">{profile?.displayName}</td>
                    </tr>
                    <tr>
                        <th>statusMessage</th>
                        <td id="statusMessageField">{profile?.statusMessage}</td>
                    </tr>
                </table>
            </div>
            {/* <!-- LIFF DATA --> */}
            <div id="liffData">
                <h2 id="liffDataHeader" className={styles.textLeft}>LIFF Data</h2>
                <table>
                    <tr>
                        <th>OS</th>
                        <td id="deviceOS" className={styles.textLeft}></td>
                    </tr>
                    <tr>
                        <th>Language</th>
                        <td id="browserLanguage" className={styles.textLeft}></td>
                    </tr>
                    <tr>
                        <th>LIFF SDK Version</th>
                        <td id="sdkVersion" className={styles.textLeft}></td>
                    </tr>
                    <tr>
                        <th>LINE Version</th>
                        <td id="lineVersion" className={styles.textLeft}></td>
                    </tr>
                    <tr>
                        <th>isInClient</th>
                        <td id="isInClient" className={styles.textLeft}></td>
                    </tr>
                    <tr>
                        <th>isLoggedIn</th>
                        <td id="isLoggedIn" className={styles.textLeft}></td>
                    </tr>
                </table>
            </div>
            {/* <!-- LOGIN LOGOUT BUTTONS --> */}
            <div className={styles.buttonGroup}>
                <button id="liffLoginButton" disabled={button.login}>Log in</button>
                <button id="liffLogoutButton" disabled={button.logout}>Log out</button>
            </div>
            <div id="statusMessage">
                <div id="isInClientMessage"></div>
                <div id="apiReferenceMessage">
                    <p>Available LIFF methods vary depending on the browser you use to open the LIFF app.</p>
                    <p>Please refer to the <a href="https://developers.line.biz/en/reference/liff/#initialize-liff-app">API reference page</a> for more information.</p>
                </div>
            </div>
        </div>
        {/* <!-- LIFF ID ERROR --> */}
        <div id="liffIdErrorMessage" className={button.liffIdErrorMessage? '':styles.hidden}>
            <p>You have not assigned any value for LIFF ID.</p>
            <p>If you are running the app using Node.js, please set the LIFF ID as an environment variable in your Heroku account follwing the below steps: </p>
            <code id="code-block">
                <ol>
                    <li>Go to `Dashboard` in your Heroku account.</li>
                    <li>Click on the app you just created.</li>
                    <li>Click on `Settings` and toggle `Reveal Config Vars`.</li>
                    <li>Set `MY_LIFF_ID` as the key and the LIFF ID as the value.</li>
                    <li>Your app should be up and running. Enter the URL of your app in a web browser.</li>
                </ol>
            </code>
            <p>If you are using any other platform, please add your LIFF ID in the <code>index.html</code> file.</p>
            <p>For more information about how to add your LIFF ID, see <a href="https://developers.line.biz/en/reference/liff/#initialize-liff-app">Initializing the LIFF app</a>.</p>
        </div>
        {/* <!-- LIFF INIT ERROR --> */}
        <div id="liffInitErrorMessage" className={button.liffInitErrorMessage? '':styles.hidden}>
            <p>Something went wrong with LIFF initialization.</p>
            <p>LIFF initialization can fail if a user clicks "Cancel" on the "Grant permission" screen, or if an error occurs in the process of <code>liff.init()</code>.</p>
        </div>
    </body>
  )
}
