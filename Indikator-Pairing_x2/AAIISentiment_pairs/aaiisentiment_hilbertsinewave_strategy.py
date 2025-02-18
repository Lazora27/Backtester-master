import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'HilbertSinewave': 1.0
        })
    )
