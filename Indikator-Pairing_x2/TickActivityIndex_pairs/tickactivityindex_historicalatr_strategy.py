import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'HistoricalATR': 1.0
        })
    )
