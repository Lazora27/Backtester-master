import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
