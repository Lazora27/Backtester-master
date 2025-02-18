import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
