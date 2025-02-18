import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'EaseOfMovement': 1.0
        })
    )
