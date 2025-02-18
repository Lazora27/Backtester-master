import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
