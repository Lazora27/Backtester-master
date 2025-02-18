import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
