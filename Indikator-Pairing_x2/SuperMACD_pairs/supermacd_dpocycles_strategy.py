import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und DPOCycles
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'DPOCycles': 1.0
        })
    )
