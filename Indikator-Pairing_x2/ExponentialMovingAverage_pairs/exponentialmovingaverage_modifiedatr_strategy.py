import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'ModifiedATR': 1.0
        })
    )
