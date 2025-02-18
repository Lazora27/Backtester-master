import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'KDJIndicator': 1.0
        })
    )
