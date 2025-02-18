import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und TrueRange
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'TrueRange': 1.0
        })
    )
