import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
