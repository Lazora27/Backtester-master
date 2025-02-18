import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
