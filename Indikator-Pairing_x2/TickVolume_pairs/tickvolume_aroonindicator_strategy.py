import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'AroonIndicator': 1.0
        })
    )
