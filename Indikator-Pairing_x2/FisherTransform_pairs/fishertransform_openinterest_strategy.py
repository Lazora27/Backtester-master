import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und OpenInterest
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'OpenInterest': 1.0
        })
    )
