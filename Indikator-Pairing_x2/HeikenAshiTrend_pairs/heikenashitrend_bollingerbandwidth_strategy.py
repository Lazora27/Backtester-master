import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
