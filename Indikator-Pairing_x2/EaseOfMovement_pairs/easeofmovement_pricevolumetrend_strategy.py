import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
