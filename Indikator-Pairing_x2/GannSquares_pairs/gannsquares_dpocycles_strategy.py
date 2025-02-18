import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und DPOCycles
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'DPOCycles': 1.0
        })
    )
