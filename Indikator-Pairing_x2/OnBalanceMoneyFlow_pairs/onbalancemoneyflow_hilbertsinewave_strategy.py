import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceMoneyFlow_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceMoneyFlow und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'OnBalanceMoneyFlow': {
                'class': OnBalanceMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceMoneyFlow'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'OnBalanceMoneyFlow': 1.0,
            'HilbertSinewave': 1.0
        })
    )
