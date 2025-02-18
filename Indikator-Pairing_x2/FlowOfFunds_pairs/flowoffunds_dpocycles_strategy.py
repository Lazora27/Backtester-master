import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und DPOCycles
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'DPOCycles': 1.0
        })
    )
