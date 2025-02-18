import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
