import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
