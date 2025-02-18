import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
