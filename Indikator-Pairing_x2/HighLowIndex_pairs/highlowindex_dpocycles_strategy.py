import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
