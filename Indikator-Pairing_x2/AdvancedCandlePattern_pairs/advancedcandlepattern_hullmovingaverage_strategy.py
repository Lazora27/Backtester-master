import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'HullMovingAverage': 1.0
        })
    )
