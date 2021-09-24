import React from 'react'

const Button = (props: any) => {
    return (
        <button
            type={props.type}
            value={props.value}
            className="inline-flex justify-center px-4 py-2 text-sm font-medium text-red-900 bg-red-100 border border-transparent rounded-md hover:bg-red-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-red-500"
            // onClick={closeModal}
        >
            {props.text}
        </button>
    )
}

export default Button
