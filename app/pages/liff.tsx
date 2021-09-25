import type { NextPage } from 'next'
import dynamic from 'next/dynamic';
import Head from 'next/head';
import React from 'react';

const LiffComponent = dynamic(
    import('../components/liff/liff'), {ssr: false}
);

const liff: NextPage = () => {
  return (
    <>
        <Head>
            <title>ラクメシ</title>
            <meta name="description" content="Generated by create next app" />
            <link rel="icon" href="/favicon.ico" />
        </Head>
        <LiffComponent />
    </>
  )
}

export default liff