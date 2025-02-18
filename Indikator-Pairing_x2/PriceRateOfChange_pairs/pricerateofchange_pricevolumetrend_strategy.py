import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
