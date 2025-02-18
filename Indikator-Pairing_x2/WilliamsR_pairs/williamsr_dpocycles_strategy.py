import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und DPOCycles
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'DPOCycles': 1.0
        })
    )
