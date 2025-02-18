import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'HistoricalATR': 1.0
        })
    )
