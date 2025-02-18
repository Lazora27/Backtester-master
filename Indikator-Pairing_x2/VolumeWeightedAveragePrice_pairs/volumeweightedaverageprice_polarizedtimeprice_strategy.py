import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeWeightedAveragePrice_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeWeightedAveragePrice und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'VolumeWeightedAveragePrice': {
                'class': VolumeWeightedAveragePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedAveragePrice'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'VolumeWeightedAveragePrice': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
