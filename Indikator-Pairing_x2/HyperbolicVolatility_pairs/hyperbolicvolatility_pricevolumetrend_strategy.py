import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
