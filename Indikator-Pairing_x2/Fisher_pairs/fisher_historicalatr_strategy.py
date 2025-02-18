import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'HistoricalATR': 1.0
        })
    )
