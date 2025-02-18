import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'HilbertSinewave': 1.0
        })
    )
