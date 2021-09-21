export interface IAuthState {
  verification: any
  verifyCode: any
  registration: any
}

export type AuthTypes = 'SMS' | 'MAIL'

export interface IGetVerificationDispatchAction {
  authType: AuthTypes
  target: string
}

export interface IVerifyCodeDispatchAction {
  code: string
  sessionToken: string
}

export interface IRegistrationDispatchAction {
  password: string
  sessionToken: string
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
