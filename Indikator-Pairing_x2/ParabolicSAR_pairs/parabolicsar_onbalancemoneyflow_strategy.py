import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_OnBalanceMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und OnBalanceMoneyFlow
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'OnBalanceMoneyFlow': {
                'class': OnBalanceMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceMoneyFlow'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'OnBalanceMoneyFlow': 1.0
        })
    )
