export type TLiffProfile = {
    userId: string | null,
    displayName: string | null,
    pictureUrl: string | null,
    statusMessage: string | null
}

export type TPreference = {
    sex: string | null,
    age: string | null,
    genre: string | null,
    budget: string | null
}

export type TCheckboxes = {
    style: boolean[],
    seat: boolean[],
    alchool: boolean[],
    facility: boolean[],
}



export type TKeyword = {
    min_budget: string | null,
    max_budget: string | null,
    keyword: string | null
}

export type TEvent = {
    style: string | null,
    date: string | null, // YY-MM-DD-dd
    location: string | null
}

export type TStyle = {
    free_drink: boolean,
    free_food: boolean,
    cource: boolean,
    lunch: boolean
}

export type TSeat = {
    private_room: boolean,
    horigotatsu: boolean,
    tatami: boolean,
    terrace: boolean
}

export type TAlchool = {
    sho: boolean,
    horigotatsu: boolean,
    tatami: boolean,
    terrace: boolean
}



