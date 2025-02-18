import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und MovingAverage
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'MovingAverage': 1.0
        })
    )
