import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und DPOCycles
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'DPOCycles': 1.0
        })
    )
