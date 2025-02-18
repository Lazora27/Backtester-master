import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
