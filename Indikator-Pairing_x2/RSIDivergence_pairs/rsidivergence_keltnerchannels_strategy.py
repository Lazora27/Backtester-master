import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'KeltnerChannels': 1.0
        })
    )
