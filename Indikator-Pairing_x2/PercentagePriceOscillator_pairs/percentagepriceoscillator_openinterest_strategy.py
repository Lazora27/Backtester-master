import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'OpenInterest': 1.0
        })
    )
