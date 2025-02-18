import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'WeightedCycle': 1.0
        })
    )
