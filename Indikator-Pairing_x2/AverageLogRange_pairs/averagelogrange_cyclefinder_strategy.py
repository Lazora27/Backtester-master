import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'CycleFinder': 1.0
        })
    )
