import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_VolumeAccumulationPercentage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und VolumeAccumulationPercentage
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'VolumeAccumulationPercentage': {
                'class': VolumeAccumulationPercentage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeAccumulationPercentage'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'VolumeAccumulationPercentage': 1.0
        })
    )
