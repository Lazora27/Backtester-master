import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
