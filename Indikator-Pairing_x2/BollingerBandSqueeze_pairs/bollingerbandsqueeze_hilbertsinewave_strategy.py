import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'HilbertSinewave': 1.0
        })
    )
