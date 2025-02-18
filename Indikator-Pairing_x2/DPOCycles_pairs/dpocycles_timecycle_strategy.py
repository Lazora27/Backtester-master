import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und TimeCycle
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'TimeCycle': 1.0
        })
    )
