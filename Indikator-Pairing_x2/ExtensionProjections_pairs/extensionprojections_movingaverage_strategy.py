import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und MovingAverage
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'MovingAverage': 1.0
        })
    )
