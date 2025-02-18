import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'HistoricalATR': 1.0
        })
    )
