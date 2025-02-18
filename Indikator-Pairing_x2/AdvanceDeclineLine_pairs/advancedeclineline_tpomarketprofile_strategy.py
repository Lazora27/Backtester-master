import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
