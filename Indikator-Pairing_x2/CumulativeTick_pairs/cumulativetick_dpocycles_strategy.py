import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und DPOCycles
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'DPOCycles': 1.0
        })
    )
