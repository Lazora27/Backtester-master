import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
