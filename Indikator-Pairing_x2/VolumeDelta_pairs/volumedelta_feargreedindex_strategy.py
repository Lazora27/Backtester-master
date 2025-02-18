import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'FearGreedIndex': 1.0
        })
    )
