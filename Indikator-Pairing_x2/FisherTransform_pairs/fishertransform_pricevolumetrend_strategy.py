import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
