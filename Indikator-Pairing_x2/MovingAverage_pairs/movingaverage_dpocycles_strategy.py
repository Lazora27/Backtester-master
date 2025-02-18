import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und DPOCycles
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'DPOCycles': 1.0
        })
    )
