import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'HilbertTrendline': 1.0
        })
    )
