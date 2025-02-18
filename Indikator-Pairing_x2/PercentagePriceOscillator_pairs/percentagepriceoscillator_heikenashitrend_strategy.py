import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
