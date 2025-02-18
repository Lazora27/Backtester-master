import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
