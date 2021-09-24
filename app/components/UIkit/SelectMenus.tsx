import React, {Fragment, useState} from 'react'
import { Listbox, Transition } from '@headlessui/react'
import { CheckIcon, SelectorIcon } from '@heroicons/react/solid'

const SelectMenus = (props: any) => {
    const [selected, setSelected] = useState(props.options[0])

    const hundleChange = async(event: any) => {
        const select_value = event
        setSelected(select_value)
        props.dispatch({type: 'change', payload: [props.label, select_value.value]})
    }

    return (
        <Listbox value={selected} onChange={hundleChange}>
        {({ open }) => (
          <>
            <Listbox.Label className="block text-lg font-medium text-gray-700">{props.title}</Listbox.Label>
            <div className="relative">
              <Listbox.Button className="relative w-full bg-white border border-gray-300 rounded-lg shadow-sm pl-3 pr-10 py-2 text-left cursor-default focus:outline-none focus:ring-1 focus:ring-red-400 focus:border-red-400 sm:text-sm">
                <span className="flex items-center">
                  <span className="ml-3 block truncate">{selected.label}</span>
                </span>
                <span className="ml-3 absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none">
                  <SelectorIcon className="h-5 w-5 text-gray-400" aria-hidden="true" />
                </span>
              </Listbox.Button>
              <Transition show={open}
                as={Fragment}
                leave="transition ease-in duration-100"
                leaveFrom="opacity-100"
                leaveTo="opacity-0"
              >
                <Listbox.Options className="absolute z-10 mt-1 w-full bg-white shadow-lg max-h-56 rounded-md py-1 text-base ring-1 ring-black ring-opacity-5 overflow-auto focus:outline-none sm:text-sm">
                  {props.options.map((option: any) => (
                    <Listbox.Option
                      key={option.value}
                      className={({active}) => `${active ? 'text-white bg-red-400' : 'text-gray-900'} cursor-default select-none relative py-2 pl-3 pr-9`}
                      value={option}
                    >
                      {({ selected, active }) => (
                        <>
                          <div className="flex items-center">
                            <span className={`${selected ? 'font-semibold' : 'font-normal'} ml-3 block truncate`} >
                              {option.label}
                            </span>
                          </div>
                          {selected ? (
                            <span className={`$(active ? 'text-white' : 'text-red-600') absolute inset-y-0 right-0 flex items-center pr-4`}>
                              <CheckIcon className="h-5 w-5" aria-hidden="true" />
                            </span>
                          ) : null}
                        </>
                      )}
                    </Listbox.Option>
                  ))}
                </Listbox.Options>
              </Transition>
            </div>
          </>
        )}
        </Listbox>
    )
}

export default SelectMenus