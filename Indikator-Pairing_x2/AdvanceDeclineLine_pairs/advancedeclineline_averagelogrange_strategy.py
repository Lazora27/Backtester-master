import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'AverageLogRange': 1.0
        })
    )
