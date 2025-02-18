import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
