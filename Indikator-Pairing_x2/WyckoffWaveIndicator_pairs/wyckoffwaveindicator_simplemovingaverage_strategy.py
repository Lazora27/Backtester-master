import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffWaveIndicator_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffWaveIndicator und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'WyckoffWaveIndicator': {
                'class': WyckoffWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffWaveIndicator'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'WyckoffWaveIndicator': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
