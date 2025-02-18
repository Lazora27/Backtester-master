import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
