import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineRatio_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineRatio und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineRatio': {
                'class': AdvanceDeclineRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineRatio'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AdvanceDeclineRatio': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
