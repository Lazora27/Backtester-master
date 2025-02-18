import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'HistoricalATR': 1.0
        })
    )
