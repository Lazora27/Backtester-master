import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
