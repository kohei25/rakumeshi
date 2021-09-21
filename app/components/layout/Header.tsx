import React from 'react'

const Header = (props: any) => {
    return (
        <div className='flex bg-red-500 w-full h-12 justify-center items-center'>
            <div className='text-lg text-white font-bold'>
                {props.title}
            </div>
        </div>
    )
}

export default Header
