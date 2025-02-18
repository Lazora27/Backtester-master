import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'HistoricalATR': 1.0
        })
    )
