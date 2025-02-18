import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und DPOCycles
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'DPOCycles': 1.0
        })
    )
