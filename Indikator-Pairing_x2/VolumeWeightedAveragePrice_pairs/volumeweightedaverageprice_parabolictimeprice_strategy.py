import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeWeightedAveragePrice_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeWeightedAveragePrice und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'VolumeWeightedAveragePrice': {
                'class': VolumeWeightedAveragePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedAveragePrice'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'VolumeWeightedAveragePrice': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
