import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'HilbertSinewave': 1.0
        })
    )
