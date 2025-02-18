import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'TRIXIndicator': 1.0
        })
    )
