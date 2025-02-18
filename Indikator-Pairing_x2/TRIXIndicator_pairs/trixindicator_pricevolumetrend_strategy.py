import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
