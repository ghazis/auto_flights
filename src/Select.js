import React from 'react';

const Select = ({ label, data, onChange, className }) => {
  let selectStyle = label == 'Duration' ? styleSheet.select : styleSheet.selectAir
  return (
    <div className={className}>
      <div style={styleSheet.label}>{label}</div>
      <select style={selectStyle} aria-label="Default select example" onChange={onChange}>
        { data.map((option, i) => {
          return <option key={i} value={option}>{option}</option>
        })}
      </select>
    </div>
  );
}

const styleSheet = {
  label: {
    color:'grey',
    fontSize: 12,
    marginBottom: 8,
    letterSpacing: 0.5
  },
  select: {
    width: 50,
    padding: 1,
    border: '1px solid grey',
    borderRadius: 3
  },
  selectAir: {
    width: 65,
    padding: 1,
    border: '1px solid grey',
    borderRadius: 3
  }
}

export default Select;