import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
