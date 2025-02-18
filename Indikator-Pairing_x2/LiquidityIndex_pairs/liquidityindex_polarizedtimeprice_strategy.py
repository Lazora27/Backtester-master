import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LiquidityIndex_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LiquidityIndex und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'LiquidityIndex': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
