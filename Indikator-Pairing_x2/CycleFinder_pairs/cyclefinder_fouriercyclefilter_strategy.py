import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
