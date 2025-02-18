import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
