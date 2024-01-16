export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = this.validateString(name, 'name');
    this._length = this.validateNumber(length, 'length');
    this._students = this.validateStudentsArray(students, 'students');
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    this._name = this.validateString(newName, 'name');
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    this._length = this.validateNumber(newLength, 'length');
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    this._students = this.validateStudentsArray(newStudents, 'students');
  }

  validateString(value, attributeName) {
    if (typeof value !== 'string') {
      throw new Error(`${attributeName} must be a string`);
    }
    return value;
  }

  validateNumber(value, attributeName) {
    if (typeof value !== 'number' || isNaN(value)) {
      throw new Error(`${attributeName} must be a valid number`);
    }
    return value;
  }

  validateStudentsArray(value, attributeName) {
    if (!Array.isArray(value) || !value.every(item => typeof item === 'string')) {
      throw new Error(`${attributeName} must be an array of strings`);
    }
    return value;
  }
}
