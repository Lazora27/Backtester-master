import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
