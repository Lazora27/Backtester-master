import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'DPOCycles': 1.0
        })
    )
