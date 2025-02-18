import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'LiquidityIndex': 1.0
        })
    )
