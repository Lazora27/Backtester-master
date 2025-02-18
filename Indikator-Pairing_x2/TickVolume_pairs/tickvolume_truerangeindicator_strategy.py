import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
