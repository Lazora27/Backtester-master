import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
