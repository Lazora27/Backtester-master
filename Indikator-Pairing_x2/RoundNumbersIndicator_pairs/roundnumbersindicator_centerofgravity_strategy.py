import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'CenterOfGravity': 1.0
        })
    )
