import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
