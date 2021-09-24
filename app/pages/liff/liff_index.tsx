import type { NextPage } from 'next'
import { useEffect, useState } from 'react'
import Head from 'next/head'
import Image from 'next/image'
import dynamic from 'next/dynamic'
import octcat from '../public/octcat.jpg'
import type liff from '@line/liff'

const Liff = dynamic(
    import('../../components/liff/liff'), {ssr: false}
);

const liff_index: NextPage = () => {

  return (
    <Liff />
  )
}

export default liff_index
