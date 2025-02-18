import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
