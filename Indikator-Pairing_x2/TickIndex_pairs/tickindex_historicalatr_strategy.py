import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'HistoricalATR': 1.0
        })
    )
