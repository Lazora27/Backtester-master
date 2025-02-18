import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
