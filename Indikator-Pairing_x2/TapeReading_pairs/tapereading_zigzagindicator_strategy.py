import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
