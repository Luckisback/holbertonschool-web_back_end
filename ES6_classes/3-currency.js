
export default class Currency {
  constructor(code, name) {
    this._code = this.validateString(code, 'code');
    this._name = this.validateString(name, 'name');
  }

  get code() {
    return this._code;
  }

  set code(newCode) {
    this._code = this.validateString(newCode, 'code');
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = this.validateString(newName, 'name');
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }

  validateString(value, attributeName) {
    if (typeof value !== 'string') {
      throw new Error(`${attributeName} must be a string`);
    }
    return value;
  }
}
