import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'HilbertTrendline': 1.0
        })
    )
