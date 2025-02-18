import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeWeightedAveragePrice_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeWeightedAveragePrice und CCITurbo
    """
    
    params = (
        ('indicators', {
            'VolumeWeightedAveragePrice': {
                'class': VolumeWeightedAveragePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeWeightedAveragePrice'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'VolumeWeightedAveragePrice': 1.0,
            'CCITurbo': 1.0
        })
    )
