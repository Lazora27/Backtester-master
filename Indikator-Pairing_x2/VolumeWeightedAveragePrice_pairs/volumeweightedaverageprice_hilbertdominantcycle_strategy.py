import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeWeightedAveragePrice_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeWeightedAveragePrice und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'VolumeWeightedAveragePrice': {
                'class': VolumeWeightedAveragePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedAveragePrice'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'VolumeWeightedAveragePrice': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
