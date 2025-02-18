import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'TRIXIndicator': 1.0
        })
    )
