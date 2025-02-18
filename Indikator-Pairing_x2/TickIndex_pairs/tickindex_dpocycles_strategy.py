import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
