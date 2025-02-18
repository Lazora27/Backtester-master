import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
