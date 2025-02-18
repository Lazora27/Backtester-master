import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'FlowOfFunds': 1.0
        })
    )
