import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
