import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'EhlersDecycler': 1.0
        })
    )
