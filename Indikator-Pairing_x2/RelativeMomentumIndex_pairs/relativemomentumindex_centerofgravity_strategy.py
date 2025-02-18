import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
