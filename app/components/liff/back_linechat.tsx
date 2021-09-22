import dynamic from 'next/dynamic'
import React from 'react'
import { closeWindow} from './init'

const back_linechat = () => {

    return (
        <button type='button' onClick={closeWindow}>
            ラインに戻る
        </button>
    )
}

export default back_linechat
