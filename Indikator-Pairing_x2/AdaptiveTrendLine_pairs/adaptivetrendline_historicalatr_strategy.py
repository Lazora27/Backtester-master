import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'HistoricalATR': 1.0
        })
    )
