import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeMomentumOscillator_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeMomentumOscillator und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'ChandeMomentumOscillator': {
                'class': ChandeMomentumOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeMomentumOscillator'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'ChandeMomentumOscillator': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
