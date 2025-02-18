import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
