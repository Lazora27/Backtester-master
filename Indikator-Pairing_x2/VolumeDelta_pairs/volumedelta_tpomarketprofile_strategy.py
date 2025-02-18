import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
