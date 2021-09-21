import { useEffect, useReducer, useState} from "react"
import { getProfile, initializeLiffOrDie } from "./init"
import SelectMenus from "../UIkit/SelectMenus"
import Button from "../UIkit/Button"
import {alchool, budget, checkboxesReducer, facility, keywordReducer, seat, style } from "./type"
import { useRouter } from "next/router"
import Spacer2 from "../layout/Spacer2"
import CheckBoxes from "../UIkit/CheckBoxes"
import Axios from 'axios'


const initialCheckboxes = {
    style: [false, false, false, false],
    seat: [false, false, false, false],
    alchool: [false, false, false, false, false],
    facility: [false, false],
}

const initialKeyword = {
    min_budget: null,
    max_budget: null,
    keyword: null
}

const input_keyword = () => {
    const router = useRouter()

    const [keyword, setKeyword] = useState('')
    const [checkboxes, cdispatch] = useReducer(checkboxesReducer, initialCheckboxes)
    const [keywords, kdispatch] = useReducer(keywordReducer, initialKeyword)
    
    useEffect(() => {
        const myLiffId = '1656441685-0MEzq1zq'
        // initializeLiffOrDie(myLiffId)
        // const userId = getProfile()
    }, [])

    function handleChange(e: any){
        setKeyword(e.target.value)
        kdispatch({type: 'change', payload: ['keyword' , e.target.value]})
    }

    function handleSubmit(event: any){
        // const iprofile = getProfile()
        // console.log(iprofile
        event.preventDefault()
        Axios.post('https://rakumeshi.loca.lt/api/input_keyword', {
            checkboxes: checkboxes,
            keywords: keywords 
        }).then(function(res){
            if(res.status == 200){
                console.log(res)
                router.push('/liff/home')
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
