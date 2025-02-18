import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'HistoricalATR': 1.0
        })
    )
