import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TRIXIndicator': 1.0
        })
    )
