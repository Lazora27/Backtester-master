import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
