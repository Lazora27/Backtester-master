import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
