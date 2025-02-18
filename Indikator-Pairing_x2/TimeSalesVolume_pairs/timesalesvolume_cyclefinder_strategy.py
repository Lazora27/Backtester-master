import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'CycleFinder': 1.0
        })
    )
