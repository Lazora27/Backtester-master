import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'SmoothedRSI': 1.0
        })
    )
