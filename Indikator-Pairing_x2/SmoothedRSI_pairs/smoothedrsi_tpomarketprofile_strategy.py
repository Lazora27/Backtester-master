import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
