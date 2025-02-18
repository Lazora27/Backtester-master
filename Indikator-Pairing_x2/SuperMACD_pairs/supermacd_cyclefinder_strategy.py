import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und CycleFinder
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'CycleFinder': 1.0
        })
    )
