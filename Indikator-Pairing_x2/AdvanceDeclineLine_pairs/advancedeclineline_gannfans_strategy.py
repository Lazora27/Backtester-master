import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und GannFans
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'GannFans': 1.0
        })
    )
