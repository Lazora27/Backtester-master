import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
