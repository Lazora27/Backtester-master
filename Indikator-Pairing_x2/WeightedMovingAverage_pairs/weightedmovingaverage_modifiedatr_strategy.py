import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'ModifiedATR': 1.0
        })
    )
