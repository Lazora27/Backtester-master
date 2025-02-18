import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TapeReading
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TapeReading': 1.0
        })
    )
