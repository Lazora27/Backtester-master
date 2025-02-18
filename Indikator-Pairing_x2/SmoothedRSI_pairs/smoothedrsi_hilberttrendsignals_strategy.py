import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
