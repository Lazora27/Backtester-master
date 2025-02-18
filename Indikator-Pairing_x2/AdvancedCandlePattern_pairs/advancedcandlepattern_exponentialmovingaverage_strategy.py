import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
