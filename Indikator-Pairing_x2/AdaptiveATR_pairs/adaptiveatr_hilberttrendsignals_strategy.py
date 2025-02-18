import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
