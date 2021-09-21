import { useEffect, useReducer} from "react"
import { getProfile, initializeLiffOrDie } from "./init"
import SelectMenus from "../UIkit/SelectMenus"
import Button from "../UIkit/Button"
import {alchool, budget, facility, seat, style } from "./type"
import { useRouter } from "next/router"
import Spacer2 from "../layout/Spacer2"
import CheckBoxes from "../UIkit/CheckBoxes"

const input_keyword = () => {
    const router = useRouter()

    // const [preference, dispatch] = useReducer(preducer, initialState)
    
    useEffect(() => {
        const myLiffId = '1656441685-0MEzq1zq'
        // initializeLiffOrDie(myLiffId)
        // const userId = getProfile()
    }, [])

    function handleSubmit(event: any){
        // const iprofile = getProfile()
        // console.log(iprofile
        event.preventDefault()
        router.push('/liff/home')
    }
    return (
        <div>
            <Spacer2 />
            <div className='text-lg text-bold'>
                予算
            </div>
            <div className='flex flex-row items-center justify-between'>
                <div className=''>
                    <SelectMenus title={''} label='min_budget' options={budget}/>
                </div>
                <div className='text-2xl text-bold'>
                    ~
                </div>
                <div className=''>
                    <SelectMenus title={''} label='max_budget' options={budget}/>
                </div>
            </div>
            <Spacer2 />
            <CheckBoxes title='形式' name='style' options={style}/>
            <Spacer2 />
            <CheckBoxes title='座席' name='seat' options={seat}/>
            <Spacer2 />
            <CheckBoxes title='お酒' name='alchool' options={alchool}/>
            <Spacer2 />
            <CheckBoxes title='設備' name='facility' options={facility}/>
            <Spacer2 />
                <input className="border-2 rounded-lg w-full text-gray-600 text-lg px-2" type="text" placeholder="キーワード (例）焼肉、渋谷" />
            <Spacer2 />
            <div className='flex justify-center'>
                <Button type='submit' value='submit' text='検索'/>
            </div>
        </div>
    )
}

export default input_keyword
