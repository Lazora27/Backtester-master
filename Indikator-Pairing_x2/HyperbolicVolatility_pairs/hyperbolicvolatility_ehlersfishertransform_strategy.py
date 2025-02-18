import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
