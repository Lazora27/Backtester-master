import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'PriceSquawk': 1.0
        })
    )
