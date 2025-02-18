import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und CycleFinder
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'CycleFinder': 1.0
        })
    )
