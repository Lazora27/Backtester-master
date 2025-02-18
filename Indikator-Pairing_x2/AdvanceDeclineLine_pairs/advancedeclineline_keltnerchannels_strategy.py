import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'KeltnerChannels': 1.0
        })
    )
