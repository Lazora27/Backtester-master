import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineRatio_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineRatio und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineRatio': {
                'class': AdvanceDeclineRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineRatio'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AdvanceDeclineRatio': 1.0,
            'KeltnerChannels': 1.0
        })
    )
