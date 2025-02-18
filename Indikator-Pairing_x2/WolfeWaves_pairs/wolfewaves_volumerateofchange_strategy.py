import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
