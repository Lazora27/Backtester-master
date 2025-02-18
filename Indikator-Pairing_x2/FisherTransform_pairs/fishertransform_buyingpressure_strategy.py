import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'BuyingPressure': 1.0
        })
    )
