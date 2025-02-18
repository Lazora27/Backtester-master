import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
