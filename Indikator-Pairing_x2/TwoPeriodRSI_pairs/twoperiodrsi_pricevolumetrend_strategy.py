import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
