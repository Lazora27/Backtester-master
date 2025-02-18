import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MultiTimeframeTrendFinder_OnBalanceMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MultiTimeframeTrendFinder und OnBalanceMoneyFlow
    """
    
    params = (
        ('indicators', {
            'MultiTimeframeTrendFinder': {
                'class': MultiTimeframeTrendFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MultiTimeframeTrendFinder'>
            },
            'OnBalanceMoneyFlow': {
                'class': OnBalanceMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceMoneyFlow'>
            }
        }),
        ('weights', {
            'MultiTimeframeTrendFinder': 1.0,
            'OnBalanceMoneyFlow': 1.0
        })
    )
