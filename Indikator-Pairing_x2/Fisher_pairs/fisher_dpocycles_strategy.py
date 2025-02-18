import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und DPOCycles
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'DPOCycles': 1.0
        })
    )
