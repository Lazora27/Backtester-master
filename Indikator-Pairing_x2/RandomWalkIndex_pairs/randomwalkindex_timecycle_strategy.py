import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
