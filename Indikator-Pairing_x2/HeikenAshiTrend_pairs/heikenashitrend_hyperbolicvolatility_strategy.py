import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
