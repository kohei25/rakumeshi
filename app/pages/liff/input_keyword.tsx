import dynamic from 'next/dynamic';
import React from 'react'
import Header from '../../components/layout/Header';
import Layout from '../../components/layout/Layout';

const InputKeywordComponents = dynamic(
    import('../../components/liff/input_keyword'), {ssr: false}
);

const input_keyword = () => {
    return (
        <div>
            <Header title='お店を検索'/>
            <Layout>
                <InputKeywordComponents />                
            </Layout>
        </div>
    )
}

export default input_keyword
