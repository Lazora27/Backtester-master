import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'SeasonalStrength': 1.0
        })
    )
