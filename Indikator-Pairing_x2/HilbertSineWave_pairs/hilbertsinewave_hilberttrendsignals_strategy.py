import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
