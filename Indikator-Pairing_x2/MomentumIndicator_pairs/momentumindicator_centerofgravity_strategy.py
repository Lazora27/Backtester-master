import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'CenterOfGravity': 1.0
        })
    )
