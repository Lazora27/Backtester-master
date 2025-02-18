import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
