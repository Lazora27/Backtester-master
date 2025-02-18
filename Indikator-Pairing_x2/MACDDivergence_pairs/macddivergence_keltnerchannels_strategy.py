import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'KeltnerChannels': 1.0
        })
    )
