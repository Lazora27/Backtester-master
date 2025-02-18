import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
