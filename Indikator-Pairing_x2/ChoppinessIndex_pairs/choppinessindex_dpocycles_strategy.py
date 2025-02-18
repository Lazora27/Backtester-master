import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
