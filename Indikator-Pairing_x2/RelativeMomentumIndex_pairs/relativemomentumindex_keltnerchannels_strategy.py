import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
