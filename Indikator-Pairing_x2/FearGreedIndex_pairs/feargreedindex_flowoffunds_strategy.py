import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
