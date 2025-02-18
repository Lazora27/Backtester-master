import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
