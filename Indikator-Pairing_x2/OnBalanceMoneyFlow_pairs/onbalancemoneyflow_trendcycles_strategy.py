import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceMoneyFlow_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceMoneyFlow und TrendCycles
    """
    
    params = (
        ('indicators', {
            'OnBalanceMoneyFlow': {
                'class': OnBalanceMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceMoneyFlow'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'OnBalanceMoneyFlow': 1.0,
            'TrendCycles': 1.0
        })
    )
