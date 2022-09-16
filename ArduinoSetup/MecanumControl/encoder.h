class encCounter {
  public:
    encCounter(byte pin) {
      _pin = pin;
    }
    long update(int direction) {
      bool curState = pinRead(_pin);
      if (_lastState != curState) {
        _lastState = curState;
        if (curState) {
          _counter += direction;
        }
      }
      return _counter;
    }

  private:
    long _counter = 0;
    byte _pin;
    bool _lastState = 0;
    // fast digitalRead for atmega328
    bool pinRead(uint8_t pin) {
      if (pin < 8) {
        return bitRead(PIND, pin);
      } else if (pin < 14) {
        return bitRead(PINB, pin - 8);
      } else if (pin < 20) {
        return bitRead(PINC, pin - 14);
      }
    }
};
