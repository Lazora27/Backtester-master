import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
