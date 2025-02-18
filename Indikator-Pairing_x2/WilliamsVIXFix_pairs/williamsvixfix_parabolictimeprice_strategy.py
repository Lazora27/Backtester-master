import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
