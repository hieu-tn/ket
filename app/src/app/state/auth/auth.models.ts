export interface IAuthState {

}

export interface ILoginDispatchAction {
  username: string
  password: string
}

export interface ILoginSuccessDispatchAction {
  challenge: string
  sessionToken?: string
  accessToken?: string
  userUuid?: string
}
