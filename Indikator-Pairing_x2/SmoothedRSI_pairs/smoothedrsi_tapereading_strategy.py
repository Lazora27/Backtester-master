import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und TapeReading
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'TapeReading': 1.0
        })
    )
