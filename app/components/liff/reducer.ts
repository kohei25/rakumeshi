import { TCheckboxes, TEvent, TKeyword, TPreference} from './type'

export type TPreferenceAction = {type: "change", payload: [string, number]}

export const preferenceReducer = (state: TPreference, action: TPreferenceAction) => {
    switch (action.type){
        case 'change':
            return {...state, [action.payload[0]]: action.payload[1]}
    }
}

export type TCheckboxesAction = {type: 'change', payload: [string, boolean[]]}

export const checkboxesReducer = (state: TCheckboxes, action: TCheckboxesAction) => {
    switch (action.type){
        case 'change':
            return {...state, [action.payload[0]]: action.payload[1]}
    }
}

export type TKeywordAction = {type: 'change', payload: [string, string]}

export const keywordReducer = (state: TKeyword, action: TKeywordAction) => {
    switch (action.type){
        case 'change':
            return {...state, [action.payload[0]]: action.payload[1]}
    }
}

export type TEventAction = {type: 'change', payload: [string, string]}

export const eventReducer = (state: TEvent, action: TEventAction) => {
    switch (action.type){
        case 'change':
            return {...state, [action.payload[0]]: action.payload[1]}
    }
}

