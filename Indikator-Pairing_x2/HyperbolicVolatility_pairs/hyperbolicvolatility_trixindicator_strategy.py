import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'TRIXIndicator': 1.0
        })
    )
