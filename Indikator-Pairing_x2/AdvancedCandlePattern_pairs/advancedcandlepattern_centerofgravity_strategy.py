import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'CenterOfGravity': 1.0
        })
    )
