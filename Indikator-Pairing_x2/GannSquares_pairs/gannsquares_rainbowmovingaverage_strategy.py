import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
