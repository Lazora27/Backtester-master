import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und DemandIndex
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'DemandIndex': 1.0
        })
    )
