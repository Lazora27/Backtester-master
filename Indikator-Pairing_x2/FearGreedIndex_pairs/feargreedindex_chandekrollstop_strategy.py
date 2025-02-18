import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
