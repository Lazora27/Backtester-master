import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und OpenInterest
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'OpenInterest': 1.0
        })
    )
