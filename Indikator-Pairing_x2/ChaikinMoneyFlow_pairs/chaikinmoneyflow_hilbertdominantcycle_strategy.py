import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinMoneyFlow_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinMoneyFlow und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ChaikinMoneyFlow': {
                'class': ChaikinMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinMoneyFlow'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ChaikinMoneyFlow': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
