import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und MovingAverage
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'MovingAverage': 1.0
        })
    )
