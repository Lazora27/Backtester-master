import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'HistoricalATR': 1.0
        })
    )
