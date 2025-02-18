import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'HistoricalATR': 1.0
        })
    )
