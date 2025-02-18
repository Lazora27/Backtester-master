import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'HistoricalATR': 1.0
        })
    )
