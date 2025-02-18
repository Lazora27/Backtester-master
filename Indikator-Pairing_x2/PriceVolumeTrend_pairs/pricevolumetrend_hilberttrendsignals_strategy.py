import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
