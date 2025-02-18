import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
