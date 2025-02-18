import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'HistoricalATR': 1.0
        })
    )
