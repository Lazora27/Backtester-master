import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
