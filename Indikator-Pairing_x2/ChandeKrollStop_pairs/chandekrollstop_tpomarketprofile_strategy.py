import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
