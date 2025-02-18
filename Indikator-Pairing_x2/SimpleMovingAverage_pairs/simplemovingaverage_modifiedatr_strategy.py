import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'ModifiedATR': 1.0
        })
    )
