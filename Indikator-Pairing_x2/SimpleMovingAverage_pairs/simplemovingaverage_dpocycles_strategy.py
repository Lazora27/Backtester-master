import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SimpleMovingAverage_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SimpleMovingAverage und DPOCycles
    """
    
    params = (
        ('indicators', {
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'SimpleMovingAverage': 1.0,
            'DPOCycles': 1.0
        })
    )
