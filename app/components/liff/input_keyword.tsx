import { useEffect, useReducer, useState} from "react"
import SelectMenus from "../UIkit/SelectMenus"
import Button from "../UIkit/Button"
import {TLiffProfile} from "./type"
import {alchool, budget, facility, seat, style} from './options'
import { useRouter } from "next/router"
import Spacer2 from "../layout/Spacer2"
import CheckBoxes from "../UIkit/CheckBoxes"
import Axios from 'axios'
import liff from '@line/liff'
import { initialCheckboxes, initialKeyword, initialProfileState } from "./initialState"
import { checkboxesReducer, keywordReducer } from "./reducer"

const input_keyword = () => {
    const router = useRouter()
    const inputKeywordURL = process.env.NEXT_PUBLIC_API_URL + '/input_keyword'

    // FIXME: state management
    const [keyword, setKeyword] = useState('')
    const [profile, setProfile] = useState<TLiffProfile | undefined>(undefined)

    const [checkboxes, cdispatch] = useReducer(checkboxesReducer, initialCheckboxes)
    const [keywords, kdispatch] = useReducer(keywordReducer, initialKeyword)
    
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
        initializeLiffOrDie(myLiffId)
    }, [])

    function handleChange(e: any){
        setKeyword(e.target.value)
        kdispatch({type: 'change', payload: ['keyword' , e.target.value]})
    }

    function handleSubmit(event: any){
        event.preventDefault()
        const userId = profile?.userId
        // TODO: form validation
        Axios.post(inputKeywordURL, {
            userId: userId,
            checkboxes: checkboxes,
            keywords: keywords 
        }).then(function(res){
            if(res.status == 200){
                console.log(res)
                router.push('/liff/back')
            }
        })
    }

    return (
        <div>
            <Spacer2 />
            <form onSubmit={handleSubmit}>
                <div className='text-lg text-bold'>
                    予算
                </div>
                <div className='flex flex-row items-center justify-between'>
                    <div className=''>
                        <SelectMenus title={''} label='min_budget' options={budget} initialState={initialKeyword['min_budget']} dispatch={kdispatch}/>
                    </div>
                    <div className='text-2xl text-bold'>
                        ~
                    </div>
                    <div className=''>
                        <SelectMenus title={''} label='max_budget' options={budget} initialState={initialKeyword['min_budget']} dispatch={kdispatch}/>
                    </div>
                </div>
                <Spacer2 />
                <CheckBoxes title='形式' name='style' options={style} initialState={initialCheckboxes['style']} dispatch={cdispatch}/>
                <Spacer2 />
                <CheckBoxes title='座席' name='seat' options={seat} initialState={initialCheckboxes['seat']} dispatch={cdispatch}/>
                <Spacer2 />
                <CheckBoxes title='お酒' name='alchool' options={alchool} initialState={initialCheckboxes['alchool']} dispatch={cdispatch}/>
                <Spacer2 />
                <CheckBoxes title='設備' name='facility' options={facility} initialState={initialCheckboxes['facility']} dispatch={cdispatch}/>
                <Spacer2 />
                <input className="border-2 rounded-lg w-full text-gray-600 text-lg px-2" type="text" placeholder="キーワード (例）焼肉、渋谷" value={keyword} onChange={handleChange}/>
                <Spacer2 />
                <div className='flex justify-center'>
                    <Button type='submit' value='submit' text='検索'/>
                </div>
            </form>
        </div>
    )
}

export default input_keyword
