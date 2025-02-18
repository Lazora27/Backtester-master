import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
