import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
