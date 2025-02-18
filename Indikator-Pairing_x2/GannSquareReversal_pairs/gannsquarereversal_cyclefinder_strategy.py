import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und CycleFinder
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'CycleFinder': 1.0
        })
    )
