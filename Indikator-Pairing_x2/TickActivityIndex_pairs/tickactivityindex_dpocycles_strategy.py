import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
