import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und DPOCycles
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'DPOCycles': 1.0
        })
    )
