import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
