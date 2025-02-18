import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
