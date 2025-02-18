import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
