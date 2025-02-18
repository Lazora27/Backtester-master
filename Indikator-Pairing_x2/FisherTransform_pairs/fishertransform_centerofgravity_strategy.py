import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'CenterOfGravity': 1.0
        })
    )
