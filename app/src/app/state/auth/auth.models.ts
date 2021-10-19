import { AuthTypes } from '@/modules/auth/auth.models';


export interface IAuthState {
  verification: IVerification | any
  verifyCode: IVerifyCode | any
  registration: boolean | any
  login: ILogin | any
}

export interface IVerification {
  sessionToken: string
  expiresIn?: string
}

export interface IVerifyCode {
  sessionToken: string
  expiresIn?: string
}

export interface ILogin {
  challenge: string
  sessionToken?: string
  accessToken?: string
  userUuid?: string
}

export interface IGetVerificationPayloadAction {
  authType: AuthTypes
  target: string
}

export interface IVerifyCodePayloadAction {
  sessionToken: string
  code: string
}

export interface IRegistrationPayloadAction {
  sessionToken: string
  password: string
}

export interface ILoginPayloadAction {
  username: string
  password: string
}
