import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'capitalize'
})
export class CapitalizePipe implements PipeTransform {

  transform(value: string, ...args: unknown[]): unknown {
    const words: Array<string> = [];
    value.split(' ').map((word: string) => {
      if (word) {
        word = word.charAt(0).toUpperCase() + word.substr(1, word.length - 1);
      }
      words.push(word);
    });

    return words.join(' ');
  }

}
