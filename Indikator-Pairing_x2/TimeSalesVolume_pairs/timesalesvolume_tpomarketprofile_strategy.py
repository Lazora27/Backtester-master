import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
