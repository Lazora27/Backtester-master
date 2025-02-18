import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'ModifiedATR': 1.0
        })
    )
