import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
