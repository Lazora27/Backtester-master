import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_HeikenAshiSmoothed_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und HeikenAshiSmoothed
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'HeikenAshiSmoothed': {
                'class': HeikenAshiSmoothed,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiSmoothed'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'HeikenAshiSmoothed': 1.0
        })
    )
