import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
