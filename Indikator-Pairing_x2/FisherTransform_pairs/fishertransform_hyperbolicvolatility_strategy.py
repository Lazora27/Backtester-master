import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
