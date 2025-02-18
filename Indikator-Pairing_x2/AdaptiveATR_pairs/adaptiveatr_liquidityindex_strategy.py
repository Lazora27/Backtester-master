import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'LiquidityIndex': 1.0
        })
    )
