import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'EaseOfMovement': 1.0
        })
    )
