import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
