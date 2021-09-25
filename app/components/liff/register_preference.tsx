import { useEffect, useReducer, useState} from "react"
import SelectMenus from "../UIkit/SelectMenus"
import Button from "../UIkit/Button"
import { TLiffProfile } from "./type"
import { preferenceReducer } from "./reducer"
import {sex, age, genre, budget_category} from './options'
import { useRouter } from "next/router"
import Spacer5 from "../layout/Spacer5"
import Axios from 'axios'
import liff from '@line/liff'
import { initialPreferenceState, initialProfileState } from "./initialState"

const register_preference = () => {
    const router = useRouter()

    const [preference, dispatch] = useReducer(preferenceReducer, initialPreferenceState)
    const [profile, setProfile] = useState<TLiffProfile | undefined>(undefined)

    const checkUserURL: string = process.env.NEXT_PUBLIC_API_URL + '/check_user'
    const registerPreferenceURL: string = process.env.NEXT_PUBLIC_API_URL + '/register_preference'

    const initializeLiffOrDie = (myLiffId: string | undefined) => {
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

    function getProfile(): [number, TLiffProfile]{
        const responce: TLiffProfile = initialProfileState
        liff.getProfile().then(function(profile: any) {
            responce.userId = profile.userId
            setProfile(responce)
            Axios.post(checkUserURL, {
                userId: responce.userId,
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
        const myLiffId = process.env.NEXT_PUBLIC_LIFFID
        initializeLiffOrDie(myLiffId)
    }, [])

    function handleSubmit(event: any){
        event.preventDefault()
        const userId = profile?.userId
        // TODO: form validation
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
                {errorMessage.sex}
                <SelectMenus title={'性別'} label='sex' options={sex} dispatch={dispatch}/>
                <Spacer5 />
                {errorMessage.age}
                <SelectMenus title={'年齢'} label='age' options={age} dispatch={dispatch}/>
                <Spacer5 />
                {errorMessage.genre}
                <SelectMenus title={'好み'} label='genre' options={genre} dispatch={dispatch}/>
                <Spacer5 />
                {errorMessage.}
                <SelectMenus title={'予算'} label='budget' options={budget_category} dispatch={dispatch}/>
                <Spacer5 />
                <div className='flex w-fll justify-center'>
                    <Button type='submit' value='submit' text={'登録する'}/>
                </div>
            </form>
        </>
    )
}

export default register_preference
