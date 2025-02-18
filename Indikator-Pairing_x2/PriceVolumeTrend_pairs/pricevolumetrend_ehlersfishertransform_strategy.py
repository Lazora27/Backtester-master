import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
