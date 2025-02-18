import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeAccumulationPercentage_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeAccumulationPercentage und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeAccumulationPercentage': {
                'class': VolumeAccumulationPercentage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeAccumulationPercentage'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'VolumeAccumulationPercentage': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
