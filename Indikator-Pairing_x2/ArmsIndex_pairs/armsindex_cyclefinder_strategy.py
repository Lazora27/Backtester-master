import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
