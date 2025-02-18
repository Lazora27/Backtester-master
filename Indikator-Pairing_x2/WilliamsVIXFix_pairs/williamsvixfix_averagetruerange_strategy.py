import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'AverageTrueRange': 1.0
        })
    )
