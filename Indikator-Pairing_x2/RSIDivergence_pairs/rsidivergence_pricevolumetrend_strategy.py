import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
