import React, { useState } from 'react';
import Grid from '@material-ui/core/Grid';
import DateFnsUtils from '@date-io/date-fns';
import {
  MuiPickersUtilsProvider,
  KeyboardDatePicker,
} from '@material-ui/pickers';

const Datepicker = ({ id, label, className, dateChangeFn }) => {
  const [selectedDate, setSelectedDate] = useState(new Date());

  return (
    <div className={className}>
      <MuiPickersUtilsProvider utils={DateFnsUtils}>
        <Grid>
          <KeyboardDatePicker
            id={id}
            disableToolbar
            variant="inline"
            format="MM/dd/yyyy"
            margin="normal"
            label={label}
            value={selectedDate}
            onChange={(date) => {setSelectedDate(date); dateChangeFn(id, date); }}
            KeyboardButtonProps={{
              'aria-label': 'change date',
            }}
          />
        </Grid>
      </MuiPickersUtilsProvider>
    </div>
  );
}

export default Datepicker