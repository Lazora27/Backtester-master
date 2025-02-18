import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
