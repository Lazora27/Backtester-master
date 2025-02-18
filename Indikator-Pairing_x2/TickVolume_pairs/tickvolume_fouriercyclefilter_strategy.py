import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
