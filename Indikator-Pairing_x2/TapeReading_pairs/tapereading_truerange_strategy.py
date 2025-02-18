import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und TrueRange
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'TrueRange': 1.0
        })
    )
