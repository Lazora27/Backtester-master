import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeAccumulationPercentage_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeAccumulationPercentage und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'VolumeAccumulationPercentage': {
                'class': VolumeAccumulationPercentage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeAccumulationPercentage'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'VolumeAccumulationPercentage': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
