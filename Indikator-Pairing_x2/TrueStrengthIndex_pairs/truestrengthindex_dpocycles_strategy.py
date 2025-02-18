import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
