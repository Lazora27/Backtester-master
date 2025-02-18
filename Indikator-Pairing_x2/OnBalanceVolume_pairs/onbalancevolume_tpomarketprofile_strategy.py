import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
