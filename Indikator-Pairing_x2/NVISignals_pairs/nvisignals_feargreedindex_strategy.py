import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'FearGreedIndex': 1.0
        })
    )
