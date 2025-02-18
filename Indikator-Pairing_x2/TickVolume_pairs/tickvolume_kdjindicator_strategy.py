import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'KDJIndicator': 1.0
        })
    )
