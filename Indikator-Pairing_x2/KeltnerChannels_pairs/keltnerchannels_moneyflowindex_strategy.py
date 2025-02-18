import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
