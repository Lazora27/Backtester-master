import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'FlowOfFunds': 1.0
        })
    )
