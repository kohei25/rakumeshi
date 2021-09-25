import liff from '@line/liff'
import Axios from 'axios'
import { useRouter } from 'next/router'
import React, { useEffect, useState } from 'react'
import Spacer5 from '../../layout/Spacer5'
import Button from '../../UIkit/Button'
import RadioButton from '../../UIkit/RadioButton'
import { initialProfileState } from '../initialState'
import { TLiffProfile } from '../type'


const options = [
    {
        label: '参加する',
        value: 0
    },
    {
        label: '参加しない',
        value: 1
    }
]

const invitation = () => {
    // expected URL => https://xxxx/liff/event/invitation?event_id=xx&date=2021-10-1-水&location=渋谷&style=飲み会
    const router = useRouter()
    const eventId = router.query['event_id']
    const date: string | string[] | undefined = router.query['date']
    let dates = ['20xx', 'x', 'x', 'x']
    if(typeof date == 'string'){
        dates = date.split('-') 
    }
    const location = router.query['location']
    const style = router.query['style']

    const invitationURL = process.env.NEXT_PUBLIC_API_URL + '/attend'

    const [profile, setProfile] = useState<TLiffProfile | undefined>(undefined)
    const [attend, setAttend] = useState()

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
        // FIXME: evable
        initializeLiffOrDie(myLiffId)
    }, [])

    function checkSelected(e: any){
        setAttend(e.value)
    }

    function handleSubmit(){
        const userId = profile?.userId 
        //TODO:  form validation
        Axios.post(invitationURL, {
            userId: userId,
            eventId: eventId,
            attend: attend
        }).then(function(res){
            if(res.status == 200){
                console.log(res)
                router.push('/liff/back')
            }
        })
    }

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <div className='font-medium'>日付</div>
                <div className='font-bold text-center'>{dates[0]}年{dates[1]}月{dates[2]}日（{dates[3]}）</div>
                <Spacer5 />
                <div className='font-medium'>場所</div>
                <div className='font-bold text-center'>{location}</div>
                <Spacer5 />
                <div className='font-medium text-center'>での{style}に参加しますか？</div>
                <RadioButton options={options} onSelected={checkSelected}/>
                <div className='flex justify-center'>
                    <Button class='bg-green-500 text-white' text='提出する' value='' />
                </div>
            </form>
        </div>
    )
}


export default invitation
