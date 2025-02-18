import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und CycleFinder
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'CycleFinder': 1.0
        })
    )
