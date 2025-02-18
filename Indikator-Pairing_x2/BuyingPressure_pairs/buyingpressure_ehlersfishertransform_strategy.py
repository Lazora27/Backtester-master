import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
