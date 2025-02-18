import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
