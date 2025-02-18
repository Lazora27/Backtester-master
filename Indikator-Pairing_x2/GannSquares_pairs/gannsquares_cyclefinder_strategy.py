import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und CycleFinder
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'CycleFinder': 1.0
        })
    )
