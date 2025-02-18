import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'FearGreedIndex': 1.0
        })
    )
