import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
