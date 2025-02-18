import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'CenterOfGravity': 1.0
        })
    )
