import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_OnBalanceMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und OnBalanceMoneyFlow
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'OnBalanceMoneyFlow': {
                'class': OnBalanceMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceMoneyFlow'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'OnBalanceMoneyFlow': 1.0
        })
    )
