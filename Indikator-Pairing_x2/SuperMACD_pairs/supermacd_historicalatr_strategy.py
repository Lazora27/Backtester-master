import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'HistoricalATR': 1.0
        })
    )
