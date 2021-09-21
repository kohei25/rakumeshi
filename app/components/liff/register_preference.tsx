import { useEffect, useReducer} from "react"
import { getProfile, initializeLiffOrDie } from "../../lib/liff/liff_init"
import SelectMenus from "../UIkit/SelectMenus"
import Button from "../UIkit/Button"
import { preducer, TPreference, sex, age, genre, budget, budget_category } from "./type"
import { useRouter } from "next/router"
import Spacer5 from "../layout/Spacer5"

const initialState = {
    sex: null,
    age: null,
    genre: null,
    budget: null
}

const register_preference = () => {
    const router = useRouter()

    const [preference, dispatch] = useReducer(preducer, initialState)
    
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
