import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
