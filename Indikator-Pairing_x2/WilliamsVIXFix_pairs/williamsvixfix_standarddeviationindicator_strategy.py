import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
