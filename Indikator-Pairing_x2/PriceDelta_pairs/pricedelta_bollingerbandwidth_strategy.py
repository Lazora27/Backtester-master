import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
