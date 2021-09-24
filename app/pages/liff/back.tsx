import { NextPage } from 'next'
import dynamic from 'next/dynamic'
import React from 'react'
import Layout from '../../components/layout/Layout'

const BackLineChatComponent = dynamic(
    import('../../components/liff/back_linechat'), {ssr: false}
)

const back: NextPage = () => {
    return (
        <div className='w-full h-full flex justify-center'>
            <BackLineChatComponent />
        </div>
    )
}

export default back
