import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und OpenInterest
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'OpenInterest': 1.0
        })
    )
