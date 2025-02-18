import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SmartOrderBlock_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SmartOrderBlock
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SmartOrderBlock': 1.0
        })
    )
