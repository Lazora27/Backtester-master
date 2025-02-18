import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und CycleFinder
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'CycleFinder': 1.0
        })
    )
