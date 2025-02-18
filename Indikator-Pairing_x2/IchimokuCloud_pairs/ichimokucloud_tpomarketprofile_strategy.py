import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
