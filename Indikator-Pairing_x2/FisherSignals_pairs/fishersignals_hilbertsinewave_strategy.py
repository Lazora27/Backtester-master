import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'HilbertSinewave': 1.0
        })
    )
