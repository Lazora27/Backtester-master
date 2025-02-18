import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_DetrendedPriceIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und DetrendedPriceIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'DetrendedPriceIndicator': {
                'class': DetrendedPriceIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'DetrendedPriceIndicator': 1.0
        })
    )
