import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und TapeReading
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'TapeReading': 1.0
        })
    )
