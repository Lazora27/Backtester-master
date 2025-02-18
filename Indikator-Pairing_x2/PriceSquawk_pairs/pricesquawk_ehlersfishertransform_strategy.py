import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
