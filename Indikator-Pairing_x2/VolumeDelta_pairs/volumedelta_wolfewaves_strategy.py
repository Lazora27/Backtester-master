import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'WolfeWaves': 1.0
        })
    )
