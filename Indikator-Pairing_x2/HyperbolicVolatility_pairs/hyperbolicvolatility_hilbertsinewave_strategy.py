import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'HilbertSinewave': 1.0
        })
    )
