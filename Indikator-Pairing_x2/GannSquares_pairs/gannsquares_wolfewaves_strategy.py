import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'WolfeWaves': 1.0
        })
    )
