import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_MomentumIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und MomentumIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'MomentumIndicator': 1.0
        })
    )
