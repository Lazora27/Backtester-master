import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
