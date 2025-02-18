import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
