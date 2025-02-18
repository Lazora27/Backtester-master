import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'HilbertTrendline': 1.0
        })
    )
