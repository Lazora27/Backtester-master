import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'DeltaProfile': 1.0
        })
    )
