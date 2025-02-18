import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'VortexIndicator': 1.0
        })
    )
