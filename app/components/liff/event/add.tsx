import router, { useRouter } from 'next/router'
import React, { useEffect, useReducer, useState } from 'react'
import Spacer2 from '../../layout/Spacer2'
import Spacer5 from '../../layout/Spacer5'
import Button from '../../UIkit/Button'
import DatePicker from '../../UIkit/DatePicker'
import { initialEvent, initialProfileState } from '../initialState'
import { eventReducer } from '../reducer'
import { TLiffProfile } from '../type'
import liff from '@line/liff'
import Axios from 'axios'
import SelectMenus from '../../UIkit/SelectMenus'
import { event_style } from '../options'
import { closeWindow} from '../init'

const add = () => {
    // expected URL => https://xxxx/liff/event/add?group_id=xx&count=yy
    const router = useRouter()
    const groupId = router.query['group_id']
    const count = router.query['count']

    // FIXME: state management
    const [location, setLoaction] = useState('')
    const [profile, setProfile] = useState<TLiffProfile | undefined>(undefined)
    const [event, dispatch] = useReducer(eventReducer, initialEvent)
    const eventAddURL = process.env.NEXT_PUBLIC_API_URL + '/event'

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
            return [0, responce]
        }).catch(function(error: any) {
            window.alert('Error getting profile: ' + error);
            return [1, responce]
        });
        return [2, responce]
    }

    useEffect(() => {
        const myLiffId = process.env.NEXT_PUBLIC_LIFFID
        // FIXME: enable
        initializeLiffOrDie(myLiffId)
    }, [])

    function handleChange(e: any){
        setLoaction(e.target.value)
        dispatch({type: 'change', payload: ['location' , e.target.value]})
    }

    function handleSubmit(e: any){
        e.preventDefault()
        const userId = profile?.userId
        // TODO: form validation
        Axios.post(eventAddURL, {
            userId: userId,
            count: count,
            event: event,
            groupId: groupId
        }).then(function(res){
            if(res.status == 200){
                console.log(res)
                closeWindow()
            }
        })
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <Spacer5 />
                <div className='block text-md'>1.  どんなイベントですか？</div>
                <Spacer2 />
                <SelectMenus title='' label='style' options={event_style} dispatch={dispatch}/>
                <Spacer5 />
                <div className='block text-md'>2.  日付を選択してください</div>
                <DatePicker name='date' dispatch={dispatch}/>
                <Spacer5 />
                <div className='block text-md'>3.  場所を入力してください</div>
                <input className="border-2 rounded-lg w-full text-gray-600 text-lg px-2 truncate" onChange={handleChange} type="text" placeholder="駅名や場所　(例： 渋谷 自由が丘)"/>
                <Spacer5 />
                <div className='flex justify-center'>
                    <Button class='bg-green-500 text-white' text='イベントを作成する' value='' />
                </div>
            </form>
        </div>
    )
}

export default add
