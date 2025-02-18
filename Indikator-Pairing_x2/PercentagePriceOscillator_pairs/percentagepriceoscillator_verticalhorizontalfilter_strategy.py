import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_VerticalHorizontalFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und VerticalHorizontalFilter
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'VerticalHorizontalFilter': {
                'class': VerticalHorizontalFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VerticalHorizontalFilter'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'VerticalHorizontalFilter': 1.0
        })
    )
