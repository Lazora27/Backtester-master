import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'CycleFinder': 1.0
        })
    )
