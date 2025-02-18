import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und CycleFinder
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'CycleFinder': 1.0
        })
    )
