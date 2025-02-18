import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und DPOCycles
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'DPOCycles': 1.0
        })
    )
