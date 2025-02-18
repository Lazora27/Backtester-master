import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'HilbertSinewave': 1.0
        })
    )
