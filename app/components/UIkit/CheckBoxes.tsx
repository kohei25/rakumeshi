import React from 'react'

const CheckBoxes = (props: any) => {
    return (
        <>
        <div className='text-lg text-bold'>
        {props.title}
        </div>
        <div className='w-full flex flex-wrap'>
            {props.options.map((option: any) => (
                <div className="flex items-center ml-2">
                    <input
                    name={props.name}
                    type="checkbox"
                    value={option.value}
                    className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
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
