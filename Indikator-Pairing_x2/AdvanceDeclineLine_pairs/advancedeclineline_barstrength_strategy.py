import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und BarStrength
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'BarStrength': 1.0
        })
    )
