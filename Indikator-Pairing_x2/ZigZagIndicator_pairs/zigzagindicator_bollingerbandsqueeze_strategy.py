import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZigZagIndicator_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZigZagIndicator und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'ZigZagIndicator': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
