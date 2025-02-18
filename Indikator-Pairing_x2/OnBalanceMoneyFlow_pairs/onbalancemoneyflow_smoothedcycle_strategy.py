import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceMoneyFlow_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceMoneyFlow und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'OnBalanceMoneyFlow': {
                'class': OnBalanceMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceMoneyFlow'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'OnBalanceMoneyFlow': 1.0,
            'SmoothedCycle': 1.0
        })
    )
