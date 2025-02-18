import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'WeightedCycle': 1.0
        })
    )
