import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
