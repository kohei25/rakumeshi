
import { useEffect} from 'react'
import liff from '@line/liff'

export default function Liff(){
    
    useEffect(() => {
        const myLiffId = process.env.NEXT_PUBLIC_LIFFID
        initializeLiffOrDie(myLiffId)
    }, [])

    const initializeLiffOrDie = (myLiffId: string | undefined) => {
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

    return (
        <div></div>
    )
}
