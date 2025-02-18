import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
