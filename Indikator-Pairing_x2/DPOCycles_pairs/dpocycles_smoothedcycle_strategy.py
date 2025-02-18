import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'SmoothedCycle': 1.0
        })
    )
