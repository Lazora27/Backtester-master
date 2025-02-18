import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'LiquidityIndex': 1.0
        })
    )
