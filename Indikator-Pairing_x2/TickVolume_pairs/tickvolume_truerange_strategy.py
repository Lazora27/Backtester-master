import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TrueRange
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TrueRange': 1.0
        })
    )
