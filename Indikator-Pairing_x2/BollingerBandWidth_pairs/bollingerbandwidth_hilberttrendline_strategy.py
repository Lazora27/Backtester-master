import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'HilbertTrendline': 1.0
        })
    )
