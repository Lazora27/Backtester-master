import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und GannAngles
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'GannAngles': 1.0
        })
    )
