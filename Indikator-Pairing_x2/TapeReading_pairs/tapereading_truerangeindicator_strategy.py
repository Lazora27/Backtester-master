import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
