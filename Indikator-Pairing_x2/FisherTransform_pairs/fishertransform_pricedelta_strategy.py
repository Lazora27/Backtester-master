import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und PriceDelta
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'PriceDelta': 1.0
        })
    )
