import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
