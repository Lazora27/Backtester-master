import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und WilliamsR
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'WilliamsR': 1.0
        })
    )
