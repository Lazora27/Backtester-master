import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
