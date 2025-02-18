import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'CenterOfGravity': 1.0
        })
    )
