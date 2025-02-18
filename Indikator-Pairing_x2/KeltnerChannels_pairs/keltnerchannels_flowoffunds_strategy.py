import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'FlowOfFunds': 1.0
        })
    )
