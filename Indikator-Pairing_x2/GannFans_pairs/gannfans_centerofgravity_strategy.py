import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'CenterOfGravity': 1.0
        })
    )
