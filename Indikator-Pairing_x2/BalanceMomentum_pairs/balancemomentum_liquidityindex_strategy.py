import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'LiquidityIndex': 1.0
        })
    )
