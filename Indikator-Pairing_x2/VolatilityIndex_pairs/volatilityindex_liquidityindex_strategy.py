import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'LiquidityIndex': 1.0
        })
    )
