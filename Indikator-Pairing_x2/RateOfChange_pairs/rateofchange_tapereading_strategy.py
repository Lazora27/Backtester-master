import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und TapeReading
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'TapeReading': 1.0
        })
    )
