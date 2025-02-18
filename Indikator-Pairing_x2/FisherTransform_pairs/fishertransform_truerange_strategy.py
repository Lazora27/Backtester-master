import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und TrueRange
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'TrueRange': 1.0
        })
    )
