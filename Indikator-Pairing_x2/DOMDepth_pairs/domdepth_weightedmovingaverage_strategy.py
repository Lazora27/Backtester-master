import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
