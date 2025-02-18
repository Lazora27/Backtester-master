import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und DPOCycles
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'DPOCycles': 1.0
        })
    )
