import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_VolumeAccumulationPercentage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und VolumeAccumulationPercentage
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'VolumeAccumulationPercentage': {
                'class': VolumeAccumulationPercentage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeAccumulationPercentage'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'VolumeAccumulationPercentage': 1.0
        })
    )
