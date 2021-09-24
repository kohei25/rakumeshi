import { useEffect, useReducer, useState} from "react"
// import { getProfile, initializeLiffOrDie } from './init'
import SelectMenus from "../UIkit/SelectMenus"
import Button from "../UIkit/Button"
import { preferenceReducer, TPreference, TDictLiffProfile, TLiffProfile } from "./type"
import {sex, age, genre, budget, budget_category} from './options'
import { useRouter } from "next/router"
import Spacer5 from "../layout/Spacer5"
import { openWindow } from "./init"
import Axios from 'axios'
import { isResSent } from "next/dist/shared/lib/utils"
import liff from '@line/liff'
import { GetStaticProps } from "next"

const initialState = {
    sex: null,
    age: null,
    genre: null,
    budget: null
}

const register_preference = () => {
    const router = useRouter()

    const [preference, dispatch] = useReducer(preferenceReducer, initialState)
    const [profile, setProfile] = useState<TLiffProfile | undefined>(undefined)

    const checkUserURL: string = process.env.NEXT_PUBLIC_API_URL + '/check_user'
    const registerPreferenceURL: string = process.env.NEXT_PUBLIC_API_URL + '/register_preference'

    const initializeLiffOrDie = (myLiffId: string) => {
        if(!myLiffId){
        } else {
            liff
            .init({
                liffId: myLiffId
            })
            .then(() => {
                if (liff.isLoggedIn()){
                    getProfile()
                } else {
                }
            })
            .catch((err: any) => {
                console.log(err)
            })
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
            Axios.post(checkUserURL, {
                userId: responce[0].userId,
            }).then(function(res){
                if(res.status == 200){
                    console.log(res)
                }
            })
            return [0, responce]
        }).catch(function(error: any) {
            window.alert('Error getting profile: ' + error);
            return [1, responce]
        });
        return [2, responce]
    }

    useEffect(() => {
        const myLiffId = '1656441685-MP4PJWPJ'
        initializeLiffOrDie(myLiffId)
    }, [])

    function handleSubmit(event: any){
        event.preventDefault()
        const userId = profile?.userId
        Axios.post(registerPreferenceURL, {
            userId: userId,
            preference: preference
        }).then(function(res){
            if(res.status == 200){
                console.log(res)
                router.push('/liff/back')
            }
        })
    }

    return (
        <>
            <form onSubmit={handleSubmit}>
                <Spacer5 />
                <SelectMenus title={'性別'} label='sex' options={sex} dispatch={dispatch}/>
                <Spacer5 />
                <SelectMenus title={'年齢'} label='age' options={age} dispatch={dispatch}/>
                <Spacer5 />
                <SelectMenus title={'好み'} label='genre' options={genre} dispatch={dispatch}/>
                <Spacer5 />
                <SelectMenus title={'予算'} label='budget' options={budget_category} dispatch={dispatch}/>
                <Spacer5 />
                <div className='flex w-fll justify-center'>
                    <Button type='submit' value='submit' text={'登録する'} />
                </div>
            </form>
        </>
    )
}

export default register_preference
