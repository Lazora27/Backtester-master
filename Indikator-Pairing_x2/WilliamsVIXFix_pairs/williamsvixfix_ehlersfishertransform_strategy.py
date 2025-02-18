import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
