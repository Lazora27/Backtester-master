import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'LiquidityIndex': 1.0
        })
    )
