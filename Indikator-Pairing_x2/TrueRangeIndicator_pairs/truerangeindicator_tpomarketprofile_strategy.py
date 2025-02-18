import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
