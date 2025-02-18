import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'WolfeWaves': 1.0
        })
    )
