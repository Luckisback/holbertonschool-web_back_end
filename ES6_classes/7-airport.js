export default class Airport {
  constructor(name, code) {
    this._name = this.validateString(name, 'name');
    this._code = this.validateString(code, 'code');
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = this.validateString(newName, 'name');
  }

  get code() {
    return this._code;
  }

  set code(newCode) {
    this._code = this.validateString(newCode, 'code');
  }

  toString() {
    return this._code;
  }

  validateString(value, attributeName) {
    if (typeof value !== 'string') {
      throw new Error(`${attributeName} must be a string`);
    }
    return value;
  }
}
