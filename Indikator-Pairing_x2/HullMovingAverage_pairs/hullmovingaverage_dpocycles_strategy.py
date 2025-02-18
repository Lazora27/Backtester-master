import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und DPOCycles
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'DPOCycles': 1.0
        })
    )
