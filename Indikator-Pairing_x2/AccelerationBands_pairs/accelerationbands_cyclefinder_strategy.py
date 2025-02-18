import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'CycleFinder': 1.0
        })
    )
