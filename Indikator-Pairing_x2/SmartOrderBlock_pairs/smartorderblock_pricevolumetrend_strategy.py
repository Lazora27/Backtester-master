import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
