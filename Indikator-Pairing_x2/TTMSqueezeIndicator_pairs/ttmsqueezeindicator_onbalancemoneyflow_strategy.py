import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TTMSqueezeIndicator_OnBalanceMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TTMSqueezeIndicator und OnBalanceMoneyFlow
    """
    
    params = (
        ('indicators', {
            'TTMSqueezeIndicator': {
                'class': TTMSqueezeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TTMSqueezeIndicator'>
            },
            'OnBalanceMoneyFlow': {
                'class': OnBalanceMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceMoneyFlow'>
            }
        }),
        ('weights', {
            'TTMSqueezeIndicator': 1.0,
            'OnBalanceMoneyFlow': 1.0
        })
    )
