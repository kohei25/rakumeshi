import type { NextPage } from 'next'
import { useEffect, useState } from 'react'
import Head from 'next/head'
import Image from 'next/image'
import dynamic from 'next/dynamic'
import styles from '../styles/Liff.module.css'
import octcat from '../public/octcat.jpg'
import type liff from '@line/liff'
import Layout from '../../components/layout/Layout'
import Header from '../../components/layout/Header'

const LiffRegisterPreferenceComponent = dynamic(
    import('../../components/liff/register_preference'), {ssr: false}
);
const register_preference: NextPage = () => {
    return (
        <>
            <Header title='好みの登録' />
            <Layout>
                <LiffRegisterPreferenceComponent />
            </Layout>
        </>
    )
}

export default register_preference
