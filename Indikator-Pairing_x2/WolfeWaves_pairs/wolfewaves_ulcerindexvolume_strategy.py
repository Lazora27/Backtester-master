import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
