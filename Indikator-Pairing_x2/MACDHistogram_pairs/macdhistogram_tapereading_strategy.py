import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TapeReading
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TapeReading': 1.0
        })
    )
