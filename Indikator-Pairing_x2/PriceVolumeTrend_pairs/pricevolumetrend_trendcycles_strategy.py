import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und TrendCycles
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'TrendCycles': 1.0
        })
    )
