import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
