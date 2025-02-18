import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'ModifiedATR': 1.0
        })
    )
