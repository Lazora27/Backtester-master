import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
