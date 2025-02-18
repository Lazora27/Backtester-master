import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'HilbertSinewave': 1.0
        })
    )
