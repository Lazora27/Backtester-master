import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'WolfeWaves': 1.0
        })
    )
