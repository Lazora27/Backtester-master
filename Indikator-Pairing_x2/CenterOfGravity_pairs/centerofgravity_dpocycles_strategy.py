import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und DPOCycles
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'DPOCycles': 1.0
        })
    )
