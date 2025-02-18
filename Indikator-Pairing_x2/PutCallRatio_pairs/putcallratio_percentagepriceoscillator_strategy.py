import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
