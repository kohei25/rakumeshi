import React, {Fragment, useState} from 'react'
import 'react-day-picker/lib/style.css'
import DayPicker from 'react-day-picker'


import MomentLocaleUtils from 'react-day-picker/moment'
import 'moment/locale/ja'

const day = {0: '日', 1: '月', 2: '火', 3: '水', 4: '木', 5: '金', 6: '土' }

const restyle =`
    .DayPicker-wrapper{
        padding-bottom: 0;
    }
    .DayPicker-Month{
        margin-top: 0;
        margin: 0;
    }
    .DayPicker-Day--selected{
        border-radius: 30%;
    }
`

const DatePicker = (props: any) => {

    const [selectedDay, setSelectedDay] = useState()

    function handleClick(e: any){
        // console.log(e) // return -> Fri Sep 24 2021 12:00:00 GMT+0900 (Japan Standard Time)
        const YY = e.getYear() - 100 + 2000
        const MM = e.getMonth() + 1
        const DD = e.getDate()
        const dd: 0|1|2|3|4|5|6 = e.getDay()
        const YYMMDDdd = YY + '-' + MM + '-' + DD + '-' + day[dd]
        setSelectedDay(e)
        props.dispatch({type: 'change', payload: [props.name, YYMMDDdd]})
    }

    const modifiers = {
        highlighted: selectedDay
      };

    return (
        <div className='flex justify-center'>
            <style>{restyle}</style>
            <DayPicker modifiers={modifiers} localeUtils={MomentLocaleUtils} locale='ja' disabledDays={{before: new Date()}} onDayClick={handleClick} selectedDays={selectedDay}/>
        </div>
    )
}

export default DatePicker