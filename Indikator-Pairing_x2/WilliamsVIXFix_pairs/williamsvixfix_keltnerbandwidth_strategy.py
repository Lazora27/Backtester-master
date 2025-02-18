import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
