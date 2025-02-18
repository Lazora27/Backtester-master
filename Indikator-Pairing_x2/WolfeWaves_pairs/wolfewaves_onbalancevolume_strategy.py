import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
