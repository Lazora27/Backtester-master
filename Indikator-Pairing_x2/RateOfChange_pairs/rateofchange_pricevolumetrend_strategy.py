import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
