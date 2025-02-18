import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
