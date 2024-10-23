const date = document.querySelector(".date");
const time = document.querySelector(".time");
const player_id = localStorage.getItem("id");

const now = new Date();
// Get today's date in the format 'YYYY-MM-DD'
const today = now.toISOString().split("T")[0];
// Set the min attribute to today's date to disable past dates
date.setAttribute("min", today);

let reservations_data = JSON.parse(
  document.currentScript.dataset.reservations.replaceAll("'", '"')
);

date.addEventListener("change", function () {
  const selectedDate = document.getElementById("selected_date");
  selectedDate.value = date.value;
  let hours = now.getHours();

  let timeDiv = "";
  let reservations_of_selected_date = [];
  let unclickable_buttons_postion = 0;

  if (now.getMinutes() > 0) hours += 1;

  // Select all reservations of selected date.
  for (let i = 0; i < reservations_data.length; ++i) {
    if (reservations_data[i][4] == date.value) {
      reservations_of_selected_date.push(reservations_data[i]);
    }
  }

  // Sort the reservations by time slots.
  reservations_of_selected_date.sort((res1, res2) => res1[3] - res2[3]);

  console.log(reservations_of_selected_date);
  for (let i = 7; i < 22; ++i) {
    console.log(timeDiv);
    if (date.value == today && hours > i) {
      timeDiv += ` <button type="button" class="btn unavailable" id = ${i}  disabled>${i}:00 - ${
        i + 1
      }:00</button>`;
      if (
        unclickable_buttons_postion < reservations_of_selected_date.length &&
        reservations_of_selected_date[unclickable_buttons_postion][3] == i
      ) {
        ++unclickable_buttons_postion;
      }
    } else if (
      unclickable_buttons_postion < reservations_of_selected_date.length
    ) {
      if (reservations_of_selected_date[unclickable_buttons_postion][3] == i) {
        if (
          reservations_of_selected_date[unclickable_buttons_postion][2] ==
          player_id
        ) {
          if (
            reservations_of_selected_date[unclickable_buttons_postion][5] ==
            "confirmed"
          ) {
            console.log("hi");
            timeDiv += ` <button type="button" class="btn confirmed" id = ${i}  disabled>${i}:00 - ${
              i + 1
            }:00</button>`;
          } else {
            timeDiv += ` <button type="button" class="btn cancelled" id = ${i}  disabled>${i}:00 - ${
              i + 1
            }:00</button>`;
          }
        } else {
          if (
            reservations_of_selected_date[unclickable_buttons_postion][5] ==
            "confirmed"
          ) {
            timeDiv += ` <button type="button" class="btn unavailable" id = ${i}  >${i}:00 - ${
              i + 1
            }:00</button>`;
          } else {
            timeDiv += ` <button type="button" class="btn available" id = ${i} >${i}:00 - ${
              i + 1
            }:00</button>`;
          }
        }
        ++unclickable_buttons_postion;
      } else {
        timeDiv += ` <button type="button" class="btn available" id = ${i}>${i}:00 - ${
          i + 1
        }:00</button>`;
      }
    } else if (date.value != "") {
      timeDiv += ` <button type="button" class="btn available" id = ${i} >${i}:00 - ${
        i + 1
      }:00</button>`;
    }
  }
  time.innerHTML = timeDiv;

  const btns = document.querySelectorAll(".btn");

  let currentSelected = null;

  btns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      if (currentSelected != null) {
        currentSelected.classList.remove("selected");
        if (currentSelected == e.currentTarget) {
          currentSelected.classList.toggle("selected");
        }
      }

      currentSelected = e.currentTarget;
      document.getElementById("selected_time").value = e.currentTarget.id;
      btn.classList.add("selected");
    });
  });
});
