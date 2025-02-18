import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'HistoricalATR': 1.0
        })
    )
