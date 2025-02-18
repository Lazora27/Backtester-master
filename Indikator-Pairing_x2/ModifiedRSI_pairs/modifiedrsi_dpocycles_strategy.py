import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'DPOCycles': 1.0
        })
    )
