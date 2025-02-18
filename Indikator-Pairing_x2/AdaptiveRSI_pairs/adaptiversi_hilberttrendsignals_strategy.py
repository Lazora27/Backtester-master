import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
