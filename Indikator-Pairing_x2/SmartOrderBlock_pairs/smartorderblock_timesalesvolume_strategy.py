import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
