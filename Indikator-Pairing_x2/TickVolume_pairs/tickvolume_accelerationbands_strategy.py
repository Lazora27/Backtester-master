import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'AccelerationBands': 1.0
        })
    )
