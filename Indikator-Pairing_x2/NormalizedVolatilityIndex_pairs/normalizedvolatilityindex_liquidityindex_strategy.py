import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NormalizedVolatilityIndex_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NormalizedVolatilityIndex und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'NormalizedVolatilityIndex': {
                'class': NormalizedVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedVolatilityIndex'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'NormalizedVolatilityIndex': 1.0,
            'LiquidityIndex': 1.0
        })
    )
