import { IAuthState } from '@/state/auth/auth.models';
import { ILoggerState } from '@/state/logger/logger.models';



export interface IAppState {
  auth: IAuthState
  logger: ILoggerState
}
