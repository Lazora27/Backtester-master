import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'HistoricalATR': 1.0
        })
    )
