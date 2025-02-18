import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'AverageLogRange': 1.0
        })
    )
