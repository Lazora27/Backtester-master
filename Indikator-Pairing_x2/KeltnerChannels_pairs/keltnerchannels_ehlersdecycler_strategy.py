import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'EhlersDecycler': 1.0
        })
    )
