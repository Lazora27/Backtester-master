import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
