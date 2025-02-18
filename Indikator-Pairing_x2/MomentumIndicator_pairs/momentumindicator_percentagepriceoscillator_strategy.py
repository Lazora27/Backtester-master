import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
