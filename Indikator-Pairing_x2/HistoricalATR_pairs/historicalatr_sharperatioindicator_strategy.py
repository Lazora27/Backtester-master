import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
