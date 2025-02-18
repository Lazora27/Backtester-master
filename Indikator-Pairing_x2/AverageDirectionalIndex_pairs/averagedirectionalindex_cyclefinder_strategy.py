import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
