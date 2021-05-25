import React from 'react';

const Table = ({ data, onClick }) => {
  return (
    <div>
      <table className="table table-striped">
        <thead className="thead-dark">
          <tr>
          {Object.keys(data[0]).map((header, i) => {
            var header = header.replace('_', ' ')
            return <th key={i}>{header}</th>
          })}
          </tr>
        </thead>
        <tbody>
          {data.map((data, i) => {
            return <tr key={i} onClick={()=>onClick(i)}>
              {Object.values(data).map((val, i) => {
                return <td key={i}>{val}</td>
              })}
            </tr>
          })}
        </tbody>
      </table>
    </div>
  );
}

export default Table;