export type TLiffProfile = {
    userId: string,
    displayName: string,
    pictureUrl: string | null,
    statusMessage: string | null
}

export type TDictLiffProfile = {
    [id: number]: TLiffProfile
}

export type TPreference = {
    sex: string | null,
    age: string | null,
    genre: string | null,
    budget: string | null
}

export type TPreferenceAction = {type: "change", payload: [string, number]}

export const preferenceReducer = (state: TPreference, action: TPreferenceAction) => {
    switch (action.type){
        case 'change':
            return {...state, [action.payload[0]]: action.payload[1]}
    }
}

export type TCheckboxes = {
    style: boolean[],
    seat: boolean[],
    alchool: boolean[],
    facility: boolean[],
}

export type TCheckboxesAction = {type: 'change', payload: [string, boolean[]]}

export const checkboxesReducer = (state: TCheckboxes, action: TCheckboxesAction) => {
    switch (action.type){
        case 'change':
            return {...state, [action.payload[0]]: action.payload[1]}
    }
}

export type TKeyword = {
    min_budget: string | null,
    max_budget: string | null,
    keyword: string | null
}

export type TKeywordAction = {type: 'change', payload: [string, string]}

export const keywordReducer = (state: TKeyword, action: TKeywordAction) => {
    switch (action.type){
        case 'change':
            return {...state, [action.payload[0]]: action.payload[1]}
    }
}

