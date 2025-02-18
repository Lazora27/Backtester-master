import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'WolfeWaves': 1.0
        })
    )
