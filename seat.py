#seat

class HandleSeats {
  constructor({ $target, handleNoise }) {
    this.$target = $target;
    this.handleNoise = handleNoise;
    this.$seats = this.$target.querySelectorAll("button");
    this.date = 0;
    this.seatType = 0;
    this.isNoise = false;
    this.firstSelected = true;
    this.selectedSeats = [];
    this.initialSetting();
  }

  initialSetting = () => {
    this.$seats.forEach((btn, i) =>
      btn.addEventListener("click", () => this.handleClickSeats(i))
    );
  };

  settingSeatType = (idx) => {     
    const seatRow = Math.floor(idx / 13);
    const seatCol = idx % 13;
    if (seatRow <= 1) {
      this.seatType = 1;
      this.settingNormalSeats();
    } else if (seatRow === 2 && seatCol < 10) {
      this.seatType = 2;
      this.settingMusseukSeats();
    } else if (seatRow === 2 && seatCol >= 10) {
      this.seatType = 3;
    }
  };

  handleClickSeats = (idx) => {
    const seat = this.$seats[idx];

    // 좌석 처음 선택시 좌석 타입 결정하기
    if (this.firstSelected) {
      this.settingSeatType(idx);
      this.firstSelected = false;
    }

    if (seat.classList.contains("clicked")) {
      // 선택 취소
      const i = this.selectedSeats.indexOf(idx);
      this.selectedSeats.splice(i, 1);
      seat.classList.remove("clicked");
    } else {
      // 좌석 선택
      this.selectedSeats.push(idx);
      seat.classList.add("clicked");
    }

    this.handleDisableSeats();
  };

  settingNormalSeats = () => {
    this.$seats.forEach((seat) => {
      if (
        seat.classList.contains("noise") ||
        seat.classList.contains("box")
      ) {
        seat.classList.add("likenoise");
      } else {
        seat.classList.remove("likenoise");
      }
    });
  };

  settingBoxSeats = () => {
    this.$seats.forEach((seat) => {
      if (seat.classList.contains("box")) {
        seat.classList.remove("likenoise");
      } else {
        seat.classList.add("likenoise");
      }
    });
  };

  settingNoiseSeats = () => {
    if (this.isNoise) {
      this.$seats.forEach((seat) => {
        if (seat.classList.contains("noise")) {
          seat.classList.remove("likenoise");
        } else {
          seat.classList.add("likenoise");
        }
      });
    } else {
      if (this.date > 0) {
        this.$seats.forEach((seat) => seat.classList.remove("likenoise"));
      } else {
        this.$seats.forEach((seat) => seat.classList.add("likenoise"));
      }
    }
  };

  handleDisableSeats = () => {
    // 백색소음 체크박스 체크 여부 확인
    // 모두 취소하고 선택한 좌석이 0개일 때 모두 활성화
    // 인원 수만큼의 좌석을 모두 선택했을 때
    const len = this.selectedSeats.length;
    if (len === 0) {
      if (!this.isNoise) {
      }
      this.$seats.forEach((seat) => {});
      this.seatType = 0;
    } else if (len === this.date) {
      this.$seats.forEach((seat, i) => {
        if (!this.selectedSeats.includes(i)) {
          seat.classList.add("likenoise");
        }
      });
    }
  };

  setDate = (date) => {
    this.totalSize = totalSize;
    this.settingHandicapSeats();
  };

  setIsNoise = (isNoise) => {
    this.isNoise = isNoise;
    this.settingHSeats();
  };
}

export default HandleSeats;
