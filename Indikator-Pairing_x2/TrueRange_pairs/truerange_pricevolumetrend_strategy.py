import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
