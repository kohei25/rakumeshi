import { useState } from 'react'
import { RadioGroup } from '@headlessui/react'

const plans = [
    {
      name: 'Startup',
      ram: '12GB',
      cpus: '6 CPUs',
      disk: '160 GB SSD disk',
    },
    {
      name: 'Business',
      ram: '16GB',
      cpus: '8 CPUs',
      disk: '512 GB SSD disk',
    },
]

const RadioButton = (props: any) => {
    const [selected, setSelected] = useState()

    function handleChange(e: any){
        setSelected(e)
        props.onSelected(e)
        console.log(e.value)
    }

    return (
        <div className="w-full px-4 py-16">
            <div className="w-full max-w-md mx-auto">
            <RadioGroup value={selected} onChange={handleChange}>
                <RadioGroup.Label className="sr-only">Server size</RadioGroup.Label>
                <div className="space-y-2">
                {props.options.map((option: any) => (
                    <RadioGroup.Option
                    key={option.label}
                    value={option}
                    className={({ active, checked }) =>
                        `${
                        active
                            ? 'ring-2 ring-offset-2 ring-offset-sky-300 ring-white ring-opacity-60'
                            : ''
                        }
                        ${
                        checked ? 'bg-blue-400 bg-opacity-75 text-white' : 'bg-white'
                        }
                        relative rounded-lg shadow-md px-5 py-4 cursor-pointer flex focus:outline-none`
                    }
                    >
                    {({ active, checked }) => (
                        <>
                        <div className="flex items-center justify-between w-full">
                            <div className="flex items-center">
                                <div className="text-xl">
                                    <RadioGroup.Label
                                    as="p"
                                    className={`font-medium  ${
                                        checked ? 'text-white' : 'text-gray-900'
                                    }`}
                                    >
                                    {option.label}
                                    </RadioGroup.Label>
                                </div>
                            </div>
                            {checked && (
                            <div className="flex-shrink-0 text-white">
                                <CheckIcon className="w-6 h-6" />
                            </div>
                            )}
                        </div>
                        </>
                    )}
                    </RadioGroup.Option>
                ))}
                </div>
            </RadioGroup>
            </div>
        </div>
    )
}

function CheckIcon(props: any) {
    return (
      <svg viewBox="0 0 24 24" fill="none" {...props}>
        <circle cx={12} cy={12} r={12} fill="#fff" opacity="0.2" />
        <path
          d="M7 13l3 3 7-7"
          stroke="#fff"
          strokeWidth={1.5}
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
    )
  }

export default RadioButton
