import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
