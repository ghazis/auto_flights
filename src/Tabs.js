import React from 'react';
import Paper from '@material-ui/core/Paper';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';

const CustomTabs = ({ data, onClick, activeTab, className }) => {

  return (
    <Paper className={className}>
      <Tabs
        value={activeTab}
        onChange={onClick}
        indicatorColor="primary"
        textColor="primary"
        variant="scrollable"
        scrollButtons="auto"
      >
        { data.map((label, i) => {
          return <Tab key={i} label={label} />
        })}
      </Tabs>
    </Paper>
  );
}

export default CustomTabs;