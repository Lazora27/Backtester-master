import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
