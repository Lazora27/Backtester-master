import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
