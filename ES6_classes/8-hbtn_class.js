export default class HolbertonClass {
  constructor(size, location) {
    this._size = this.validateNumber(size, 'size');
    this._location = this.validateString(location, 'location');
  }

  get size() {
    return this._size;
  }

  set size(newSize) {
    this._size = this.validateNumber(newSize, 'size');
  }

  get location() {
    return this._location;
  }

  set location(newLocation) {
    this._location = this.validateString(newLocation, 'location');
  }

  // Casting to Number returns the size
  valueOf() {
    return this._size;
  }

  // Casting to String returns the location
  toString() {
    return this._location;
  }

  validateNumber(value, attributeName) {
    if (typeof value !== 'number' || isNaN(value)) {
      throw new Error(`${attributeName} must be a valid number`);
    }
    return value;
  }

  validateString(value, attributeName) {
    if (typeof value !== 'string') {
      throw new Error(`${attributeName} must be a string`);
    }
    return value;
  }
}

