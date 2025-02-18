import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'HilbertSinewave': 1.0
        })
    )
