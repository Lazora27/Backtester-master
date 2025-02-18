import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
