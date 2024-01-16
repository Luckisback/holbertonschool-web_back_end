const brandSymbol = Symbol('brand');
const motorSymbol = Symbol('motor');
const colorSymbol = Symbol('color');

export default class Car {
  constructor(brand, motor, color) {
    this[brandSymbol] = this.validateString(brand, 'brand');
    this[motorSymbol] = this.validateString(motor, 'motor');
    this[colorSymbol] = this.validateString(color, 'color');
  }

  get brand() {
    return this[brandSymbol];
  }

  set brand(newBrand) {
    this[brandSymbol] = this.validateString(newBrand, 'brand');
  }

  get motor() {
    return this[motorSymbol];
  }

  set motor(newMotor) {
    this[motorSymbol] = this.validateString(newMotor, 'motor');
  }

  get color() {
    return this[colorSymbol];
  }

  set color(newColor) {
    this[colorSymbol] = this.validateString(newColor, 'color');
  }

  cloneCar() {
    const clone = Object.create(Object.getPrototypeOf(this));
    Object.defineProperties(clone, Object.getOwnPropertyDescriptors(this));
    return clone;
  }

  validateString(value, attributeName) {
    if (typeof value !== 'string') {
      throw new Error(`${attributeName} must be a string`);
    }
    return value;
  }
}
