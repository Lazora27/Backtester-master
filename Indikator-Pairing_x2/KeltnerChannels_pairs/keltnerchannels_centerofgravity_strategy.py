import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'CenterOfGravity': 1.0
        })
    )
