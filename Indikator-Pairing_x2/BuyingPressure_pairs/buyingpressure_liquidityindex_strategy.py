import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'LiquidityIndex': 1.0
        })
    )
