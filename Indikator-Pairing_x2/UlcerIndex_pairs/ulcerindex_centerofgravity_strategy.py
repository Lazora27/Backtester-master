import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
