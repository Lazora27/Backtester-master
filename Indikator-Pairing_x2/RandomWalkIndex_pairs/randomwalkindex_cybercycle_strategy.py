import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und CyberCycle
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'CyberCycle': 1.0
        })
    )
