import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
