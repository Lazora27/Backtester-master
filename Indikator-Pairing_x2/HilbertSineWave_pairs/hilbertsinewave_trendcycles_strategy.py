import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und TrendCycles
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'TrendCycles': 1.0
        })
    )
