import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'HistoricalATR': 1.0
        })
    )
