import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und MovingAverage
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'MovingAverage': 1.0
        })
    )
