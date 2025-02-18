import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
