import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'SmoothedCycle': 1.0
        })
    )
