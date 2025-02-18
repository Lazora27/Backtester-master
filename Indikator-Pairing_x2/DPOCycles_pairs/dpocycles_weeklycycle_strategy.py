import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'WeeklyCycle': 1.0
        })
    )
