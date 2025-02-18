import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und OpenInterest
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'OpenInterest': 1.0
        })
    )
