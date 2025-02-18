import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'PhaseDivergence': 1.0
        })
    )
