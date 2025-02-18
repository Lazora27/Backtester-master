import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
