import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'FearGreedIndex': 1.0
        })
    )
