import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
