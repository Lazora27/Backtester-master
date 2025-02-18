import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
