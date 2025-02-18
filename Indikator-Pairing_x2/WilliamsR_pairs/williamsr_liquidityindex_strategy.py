import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'LiquidityIndex': 1.0
        })
    )
