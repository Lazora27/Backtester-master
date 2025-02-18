import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'DPOCycles': 1.0
        })
    )
