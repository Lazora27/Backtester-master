import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'LiquidityIndex': 1.0
        })
    )
