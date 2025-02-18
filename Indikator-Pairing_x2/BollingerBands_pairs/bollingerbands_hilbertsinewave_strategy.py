import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'HilbertSinewave': 1.0
        })
    )
