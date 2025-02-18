import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'EaseOfMovement': 1.0
        })
    )
