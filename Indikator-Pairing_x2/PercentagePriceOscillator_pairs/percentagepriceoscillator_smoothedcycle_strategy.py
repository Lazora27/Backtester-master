import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'SmoothedCycle': 1.0
        })
    )
