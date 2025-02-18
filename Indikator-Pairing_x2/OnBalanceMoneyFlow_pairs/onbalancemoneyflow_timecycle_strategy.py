import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceMoneyFlow_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceMoneyFlow und TimeCycle
    """
    
    params = (
        ('indicators', {
            'OnBalanceMoneyFlow': {
                'class': OnBalanceMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceMoneyFlow'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'OnBalanceMoneyFlow': 1.0,
            'TimeCycle': 1.0
        })
    )
