import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und BarStrength
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'BarStrength': 1.0
        })
    )
