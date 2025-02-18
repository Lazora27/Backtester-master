import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'HistoricalATR': 1.0
        })
    )
