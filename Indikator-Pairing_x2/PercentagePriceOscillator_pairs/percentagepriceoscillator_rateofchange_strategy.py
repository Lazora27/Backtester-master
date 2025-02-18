import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und RateOfChange
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'RateOfChange': 1.0
        })
    )
