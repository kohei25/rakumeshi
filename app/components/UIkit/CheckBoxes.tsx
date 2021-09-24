import React, {useState} from 'react'

const CheckBoxes = (props: any) => {
    const [checked, setchecked] = useState(props.initialState)

    function handleChange(e: any){
        const checked_list = checked
        const new_checked = !checked[e.target.value]
        checked_list[e.target.value] = new_checked
        setchecked(checked_list)
        props.dispatch({type: 'change', payload: [props.name, checked_list]})
    }

    return (
        <>
        <div className='text-lg text-bold'>
        {props.title}
        </div>
        <div className='w-full flex flex-wrap'>
            {props.options.map((option: any, index: number) => (
                <div className="flex items-center ml-2" key={index}>
                    <input
                    name={props.name}
                    type="checkbox"
                    value={index}
                    className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                    checked={checked[index]}
                    onChange={handleChange}
                    />
                    <label htmlFor="remember-me" className="ml-1 block text-gray-900">
                    {option.label}
                    </label>
                </div>
            ))}
        </div>
        </>
    )
}

export default CheckBoxes
