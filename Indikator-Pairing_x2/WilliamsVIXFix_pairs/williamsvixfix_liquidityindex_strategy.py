import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'LiquidityIndex': 1.0
        })
    )
