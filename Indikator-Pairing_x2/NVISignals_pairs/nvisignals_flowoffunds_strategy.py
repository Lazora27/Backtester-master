import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'FlowOfFunds': 1.0
        })
    )
