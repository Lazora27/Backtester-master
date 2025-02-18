import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'FlowOfFunds': 1.0
        })
    )
