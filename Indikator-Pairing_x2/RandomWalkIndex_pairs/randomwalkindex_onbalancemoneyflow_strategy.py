import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_OnBalanceMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und OnBalanceMoneyFlow
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'OnBalanceMoneyFlow': {
                'class': OnBalanceMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceMoneyFlow'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'OnBalanceMoneyFlow': 1.0
        })
    )
