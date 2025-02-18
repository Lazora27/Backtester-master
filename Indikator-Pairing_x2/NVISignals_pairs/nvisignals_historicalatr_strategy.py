import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'HistoricalATR': 1.0
        })
    )
