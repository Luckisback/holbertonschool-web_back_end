export default class Building {
  constructor(sqft) {
    this._sqft = this.validateNumber(sqft, 'sqft');
  }

  get sqft() {
    return this._sqft;
  }

  validateNumber(value, attributeName) {
    if (typeof value !== 'number' || isNaN(value)) {
      throw new Error(`${attributeName} must be a valid number`);
    }
    return value;
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
