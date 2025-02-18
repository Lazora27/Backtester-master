import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
