import { AbstractControl, FormGroup, ValidationErrors, ValidatorFn } from '@angular/forms';
import { CODE_REGEX, PHONE_REGEX } from '@/constants/common';


export const formControlError = (form: FormGroup, fieldName: string): boolean | undefined => {
  return form.controls[fieldName]?.invalid || form.controls[fieldName]?.dirty;
};

export const PhoneRegexValidator = (): ValidatorFn => {
  const re = new RegExp(PHONE_REGEX);

  return (control: AbstractControl): ValidationErrors | null => {
    const isValid = re.test(control.value);
    return !isValid ? {phoneRegex: true} : null;
  };
};

export const CodeRegexValidator = (): ValidatorFn => {
  const re = new RegExp(CODE_REGEX);

  return (control: AbstractControl): ValidationErrors | null => {
    const isValid = re.test(control.value);
    return !isValid ? {codeRegex: true} : null;
  };
};
