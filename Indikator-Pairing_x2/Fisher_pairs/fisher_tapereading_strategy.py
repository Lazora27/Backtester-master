import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TapeReading
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TapeReading': 1.0
        })
    )
