import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'CenterOfGravity': 1.0
        })
    )
