import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'HistoricalATR': 1.0
        })
    )
