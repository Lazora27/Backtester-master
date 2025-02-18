import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
