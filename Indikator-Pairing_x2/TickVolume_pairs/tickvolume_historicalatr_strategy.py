import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'HistoricalATR': 1.0
        })
    )
