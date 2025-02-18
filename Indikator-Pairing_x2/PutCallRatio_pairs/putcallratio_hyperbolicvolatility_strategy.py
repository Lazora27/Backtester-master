import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
