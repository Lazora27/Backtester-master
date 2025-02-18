import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
