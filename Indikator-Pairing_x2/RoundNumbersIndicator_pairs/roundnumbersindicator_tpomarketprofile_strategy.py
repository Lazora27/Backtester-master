import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
