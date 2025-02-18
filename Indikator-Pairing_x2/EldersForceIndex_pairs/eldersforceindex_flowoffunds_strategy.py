import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
