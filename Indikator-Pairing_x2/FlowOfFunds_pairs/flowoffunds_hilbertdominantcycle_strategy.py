import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
