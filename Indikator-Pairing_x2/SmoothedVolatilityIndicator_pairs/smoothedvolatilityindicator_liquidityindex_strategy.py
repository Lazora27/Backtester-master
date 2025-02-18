import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedVolatilityIndicator_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedVolatilityIndicator und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedVolatilityIndicator': {
                'class': SmoothedVolatilityIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedVolatilityIndicator'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'SmoothedVolatilityIndicator': 1.0,
            'LiquidityIndex': 1.0
        })
    )
