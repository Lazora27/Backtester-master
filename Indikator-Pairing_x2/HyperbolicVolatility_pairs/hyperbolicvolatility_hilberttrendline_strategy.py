import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'HilbertTrendline': 1.0
        })
    )
