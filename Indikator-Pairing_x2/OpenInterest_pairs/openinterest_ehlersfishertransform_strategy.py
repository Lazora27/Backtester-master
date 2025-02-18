import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
