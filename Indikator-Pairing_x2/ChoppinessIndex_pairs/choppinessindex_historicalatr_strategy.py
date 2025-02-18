import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'HistoricalATR': 1.0
        })
    )
