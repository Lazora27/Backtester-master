import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
