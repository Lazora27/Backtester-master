import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
