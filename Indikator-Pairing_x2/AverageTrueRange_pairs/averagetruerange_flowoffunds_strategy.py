import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'FlowOfFunds': 1.0
        })
    )
