import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
