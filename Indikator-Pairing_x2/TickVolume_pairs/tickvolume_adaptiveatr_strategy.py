import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'AdaptiveATR': 1.0
        })
    )
