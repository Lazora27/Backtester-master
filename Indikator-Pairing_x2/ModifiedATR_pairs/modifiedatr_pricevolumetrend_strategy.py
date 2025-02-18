import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
